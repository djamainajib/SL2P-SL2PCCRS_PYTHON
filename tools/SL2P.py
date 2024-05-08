import os
import dictionariesSL2P, toolsNets
import numpy 
from datetime import datetime
import pandas as pd

def apply_net(DF,variableName,imageCollectionName,algorithm,partition=1):
    sl2p_inp=DF.values.T
    sl2p_inp=numpy.reshape(sl2p_inp,(sl2p_inp.shape[0],sl2p_inp.shape[1],-1))
    networkOptions= dictionariesSL2P.make_net_options()
    collectionOptions = (dictionariesSL2P.make_collection_options(algorithm))
    netOptions=networkOptions[variableName][imageCollectionName]
    colOptions=collectionOptions[imageCollectionName]
    
    # prepare SL2P networks
    SL2P,errorsSL2P=makeModel(algorithm,netOptions,colOptions) 
    
    # run SL2P
    print('Run SL2P...\nSL2P start: %s' %(datetime.now()))
    outDF=pd.DataFrame()
    outDF['estimate'+variableName],   outDF['networkID']  = toolsNets.wrapperNNets(SL2P      ,netOptions,colOptions,sl2p_inp,partition=partition)
    outDF['error'+variableName],Network_Ind_uncertainty     = toolsNets.wrapperNNets(errorsSL2P,netOptions,colOptions,sl2p_inp,partition=partition)
    print('SL2P end: %s' %(datetime.now()))
    
    # generate sl2p input data flag
    outDF['QC_input']=invalidInput(sl2p_inp,netOptions,colOptions)
    # generate sl2p output product flag
    outDF['QC_output']=invalidOutput(outDF.loc[:,'estimate'+variableName],netOptions)
    print('Done')
    return outDF

def SL2PCCRS (samplesDF,variableName,imageCollectionName,sl2p_inputs_bands):
    print('Estimating %s from %s data using SL2P-CCRS' %(variableName,imageCollectionName, ))
    import SL2PV1 as algorithm
    collectionOptions = (dictionariesSL2P.make_collection_options(algorithm))
    outDF=pd.DataFrame()
    if 'partition' not in samplesDF.columns:
        raise ValueError("""You should provide partition column when using SL2P-CCRS!!   """
                """Partition dictionary:  %s"""%({ff['properties']['SL2P Network']:ff['properties']['Value'] for ff in collectionOptions[imageCollectionName]["legend"]['features']}))         
    else:
        for partition in numpy.unique(samplesDF['partition']):
            samplesDF0=samplesDF[samplesDF['partition']==partition]
            samplesDF0=samplesDF0[sl2p_inputs_bands]
            outDF0=apply_net(samplesDF0,variableName,imageCollectionName,algorithm,partition=partition)
            outDF0=outDF0.set_index(samplesDF0.index)
            outDF0['partition']=partition
            outDF=pd.concat([outDF,outDF0],axis=0)  
    return outDF.sort_index()
                       
def SL2P (samplesDF,variableName,imageCollectionName,sl2p_inputs_bands):
    print('Estimating %s from %s data using SL2P-V0 [Marie Weiss]' %(variableName,imageCollectionName, ))
    import SL2PV0 as algorithm
    samplesDF=samplesDF[sl2p_inputs_bands]
    return apply_net(samplesDF,variableName,imageCollectionName,algorithm)
    
def makeModel(algorithm,netOptions,colOptions):
    numNets =len({k: v for k, v in (colOptions["Network_Ind"]['features'][0]['properties']).items() if k not in ['Feature Index','lon']}) 
    SL2P_nets =[toolsNets.makeNetVars(colOptions["Collection_SL2P"],numNets,netNum) for netNum in range(colOptions['numVariables'])]
    errorsSL2P_nets =[toolsNets.makeNetVars(colOptions["Collection_SL2Perrors"],numNets,netNum) for netNum in range(colOptions['numVariables'])]
    return SL2P_nets,errorsSL2P_nets
        
def invalidInput(image,netOptions,colOptions):
    print('Generating sl2p input data flag')
    [d0,d1,d2]=image.shape
    sl2pDomain=numpy.sort(numpy.array([row['properties']['DomainCode'] for row in colOptions["sl2pDomain"]['features']]))
    bandList={b:netOptions["inputBands"].index(b) for b in netOptions["inputBands"] if not b.startswith('cos')}
    image=image.reshape(image.shape[0],image.shape[1]*image.shape[2])[list(bandList.values()),:]

    #Image formatting
    image_format=numpy.sum((numpy.uint8(numpy.ceil(image*10)%10))* numpy.array([10**value for value in range(len(bandList))])[:,None],axis=0)
    
    # Comparing image to sl2pDomain
    flag=numpy.isin(image_format, sl2pDomain,invert=True).astype(int)
    return flag.reshape(d1*d2)

def invalidOutput(estimate,netOptions):
    print('Generating sl2p output product flag')
    return numpy.where((estimate<netOptions['outmin']) | (estimate>netOptions['outmax']),1,0)
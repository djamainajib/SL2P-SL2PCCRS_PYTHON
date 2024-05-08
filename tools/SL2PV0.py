import pickle

    
 # --------------------
 # Sentinel2 Functions: 
 # --------------------
def s2_createFeatureCollection_estimates():
    with open('nets/s2_20m_sl2p.pkl', "rb") as fp:   #Pickling
        file = pickle.load(fp)
    fp.close()    
    return file

def s2_createFeatureCollection_errors():
    with open('nets/s2_20m_sl2p_error.pkl', "rb") as fp:   #Pickling
        file = pickle.load(fp)
    fp.close()    
    return file

def s2_createFeatureCollection_domains():
    with open('nets/s2_20m_sl2p_domain.pkl', "rb") as fp:   #Pickling
        file = pickle.load(fp)
    fp.close()    
    return file

def s2_createFeatureCollection_Network_Ind():
    with open('nets/s2_20m_sl2p_parameter_file.pkl', "rb") as fp:   #Pickling
        file = pickle.load(fp)
    fp.close()    
    return file

def s2_createFeatureCollection_legend():
    with open('nets/s2_20m_sl2p_legend.pkl', "rb") as fp:   #Pickling
        file = pickle.load(fp)
    fp.close()    
    return file


 # Same functions as above using 10 m bands:   
def s2_10m_createFeatureCollection_estimates():
    with open('nets/s2_10m_sl2p.pkl', "rb") as fp:   #Pickling
        file = pickle.load(fp)
    fp.close()    
    return file

def s2_10m_createFeatureCollection_errors():
    with open('nets/s2_10m_sl2p_error.pkl', "rb") as fp:   #Pickling
        file = pickle.load(fp)
    fp.close()    
    return file

def s2_10m_createFeatureCollection_domains():
    with open('nets/s2_10m_sl2p_domain.pkl', "rb") as fp:   #Pickling
        file = pickle.load(fp)
    fp.close()    
    return file

def s2_10m_createFeatureCollection_Network_Ind():
    with open('nets/s2_10m_sl2p_parameter_file.pkl', "rb") as fp:   #Pickling
        file = pickle.load(fp)
    fp.close()    
    return file   

def s2_10m_createFeatureCollection_legend():
    with open('nets/s2_10m_sl2p_legend.pkl', "rb") as fp:   #Pickling
        file = pickle.load(fp)
    fp.close()    
    return file

 # --------------------
 # Landsat-8 Functions: 
 # --------------------
def l8_createFeatureCollection_estimates():
    with open('nets/l8_sl2p.pkl', "rb") as fp:   #Pickling
        file = pickle.load(fp)
    fp.close()    
    return file

def l8_createFeatureCollection_errors():
    with open('nets/l8_sl2p_error.pkl', "rb") as fp:   #Pickling
        file = pickle.load(fp)
    fp.close()    
    return file

def l8_createFeatureCollection_domains():
    with open('nets/l8_sl2p_domain.pkl', "rb") as fp:   #Pickling
        file = pickle.load(fp)
    fp.close()    
    return file

def l8_createFeatureCollection_Network_Ind():
    with open('nets/l8_sl2p_parameter_file.pkl', "rb") as fp:   #Pickling
        file = pickle.load(fp)
    fp.close()    
    return file

def l8_createFeatureCollection_legend():
    with open('nets/l8_sl2p_legend.pkl', "rb") as fp:   #Pickling
        file = pickle.load(fp)
    fp.close()    
    return file

 # --------------------
 # Landsat-9 Functions: 
 # --------------------
def l9_createFeatureCollection_estimates():
    with open('nets/l9_sl2p.pkl', "rb") as fp:   #Pickling
        file = pickle.load(fp)
    fp.close()    
    return file

def l9_createFeatureCollection_errors():
    with open('nets/l9_sl2p_error.pkl', "rb") as fp:   #Pickling
        file = pickle.load(fp)
    fp.close()    
    return file

def l9_createFeatureCollection_domains():
    with open('nets/l9_sl2p_domain.pkl', "rb") as fp:   #Pickling
        file = pickle.load(fp)
    fp.close()    
    return file

def l9_createFeatureCollection_Network_Ind():
    with open('nets/l9_sl2p_parameter_file.pkl', "rb") as fp:   #Pickling
        file = pickle.load(fp)
    fp.close()    
    return file

def l9_createFeatureCollection_legend():
    with open('nets/l9_sl2p_legend.pkl', "rb") as fp:   #Pickling
        file = pickle.load(fp)
    fp.close()    
    return file
 



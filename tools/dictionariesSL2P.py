  
    
    
def make_collection_options(fc): 
    COLLECTION_OPTIONS = {
        #Sentinel 2 using 20 m bands:
        'S2_L2A': {
        "Collection_SL2P": fc.s2_createFeatureCollection_estimates(),   
        "Collection_SL2Perrors": fc.s2_createFeatureCollection_errors(),        
        "sl2pDomain": fc.s2_createFeatureCollection_domains(),   
        "Network_Ind": fc.s2_createFeatureCollection_Network_Ind(), 
        "legend": fc.s2_createFeatureCollection_legend(),
        "numVariables": 7,
        "exportRes": 20,
        },
         # Sentinel 2 using 10 m bands:
        'S2_L2A_10m': {
        "Collection_SL2P": fc.s2_10m_createFeatureCollection_estimates(),
        "Collection_SL2Perrors": fc.s2_10m_createFeatureCollection_errors(),  
        "sl2pDomain": fc.s2_10m_createFeatureCollection_domains(),
        "Network_Ind": fc.s2_10m_createFeatureCollection_Network_Ind(),
        "legend": fc.s2_10m_createFeatureCollection_legend(),
        "numVariables": 7,
        "exportRes": 10,
        },
        'LC08_T1L2': {
        "Collection_SL2P": fc.l8_createFeatureCollection_estimates(),
        "Collection_SL2Perrors": fc.l8_createFeatureCollection_errors(),
        "sl2pDomain": fc.l8_createFeatureCollection_domains(),
        "Network_Ind": fc.l8_createFeatureCollection_Network_Ind(),
        "legend": fc.l8_createFeatureCollection_legend(),
        "numVariables": 7,
        "exportRes": 30,
        },
        'LC09_T1L2': {
        "Collection_SL2P": fc.l9_createFeatureCollection_estimates(),
        "Collection_SL2Perrors": fc.l9_createFeatureCollection_errors(),
        "sl2pDomain": fc.l9_createFeatureCollection_domains(),
        "Network_Ind": fc.l9_createFeatureCollection_Network_Ind(),
        "legend": fc.l9_createFeatureCollection_legend(),
        "numVariables": 7,
        "exportRes": 30,
        },
        'HLSL30': {
        "Collection_SL2P": fc.l8_createFeatureCollection_estimates(),
        "Collection_SL2Perrors": fc.l8_createFeatureCollection_errors(),
        "sl2pDomain": fc.l8_createFeatureCollection_domains(),
        "Network_Ind": fc.l8_createFeatureCollection_Network_Ind(),
        "legend": fc.l8_createFeatureCollection_legend(),
        "numVariables": 7,
        "exportRes": 30,
        }
    }
    return(COLLECTION_OPTIONS)


def make_net_options():
    NET_OPTIONS = {
        'Albedo': {
            "S2_L2A": {
                "description": 'Black sky albedo',
                "variable": 6,
                "inputBands":      ['cosVZA', 'cosSZA', 'cosRAA', 'B03', 'B04', 'B05', 'B06', 'B07', 'B8A', 'B11', 'B12'],
                "inputScaling":    [0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001],
                "inputOffset":     [-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000],
                "outmin": 0,
                "outmax": 0.2
            },
            "S2_L2A_10m": {
                "description": 'Black sky albedo',
                "variable": 6,
                "inputBands":      ['cosVZA', 'cosSZA', 'cosRAA', 'B02', 'B03', 'B04', 'B08'],
                "inputScaling":    [0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001],
                "inputOffset":     [-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000],
                "outmin": 0,
                "outmax": 0.2
            },
            'LC08_T1L2': {
                "description": 'Black sky albedo',
                "variable": 6,
                "inputBands":      ['cosVZA','cosSZA','cosRAA','SR_B3', 'SR_B4', 'SR_B5', 'SR_B6', 'SR_B7'],
                "inputScaling":     [0.0001,0.0001,0.0001,2.75e-05,2.75e-05,2.75e-05,2.75e-05,2.75e-05],
                "inputOffset":     [0,0,0,-0.2,-0.2,-0.2,-0.2,-0.2],
                "outmin": 0,
                "outmax": 0.2
            },
            'LC09_T1L2': {
                "description": 'Black sky albedo',
                "variable": 6,
                "inputBands":      ['cosVZA','cosSZA','cosRAA','SR_B3', 'SR_B4', 'SR_B5', 'SR_B6', 'SR_B7'],
                "inputScaling":     [0.0001,0.0001,0.0001,2.75e-05,2.75e-05,2.75e-05,2.75e-05,2.75e-05],
                "inputOffset":     [0,0,0,-0.2,-0.2,-0.2,-0.2,-0.2],
                "outmin": 0,
                "outmax": 0.2
            },
            'HLSL30': {
                "description": 'Black sky albedo',
                "variable": 6,
                "inputBands":      ['cosVZA','cosSZA','cosRAA','B3', 'B4', 'B5', 'B6', 'B7'],
                "inputScaling":     [0.0001,.0001,.0001,1,1,1,1,1],
                "inputOffset":     [0,0,0,0,0,0,0,0],
                "outmin": 0,
                "outmax": 0.2
            }
        },
        'fAPAR': {
            "S2_L2A": {
                "description": 'Fraction of absorbed photosynthetically active radiation',
                "variable": 2,
                "inputBands":      ['cosVZA', 'cosSZA', 'cosRAA', 'B03', 'B04', 'B05', 'B06', 'B07', 'B8A', 'B11', 'B12'],
                "inputScaling":    [0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001],
                "inputOffset":     [-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000],
                "outmin": 0,
                "outmax": 1
            },
            "S2_L2A_10m": {
                "description": 'Fraction of absorbed photosynthetically active radiation',
                "variable": 2,
                "inputBands":      ['cosVZA', 'cosSZA', 'cosRAA', 'B02', 'B03', 'B04', 'B08'],
                "inputScaling":    [0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001],
                "inputOffset":     [-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000],
                "outmin": 0,
                "outmax": 1
            },
            'LC08_T1L2': {
                "description": 'Fraction of absorbed photosynthetically active radiation',
                "variable": 2,
                "inputBands":      ['cosVZA','cosSZA','cosRAA','SR_B3', 'SR_B4', 'SR_B5', 'SR_B6', 'SR_B7'],
                "inputScaling":     [0.0001,0.0001,0.0001,2.75e-05,2.75e-05,2.75e-05,2.75e-05,2.75e-05],
                "inputOffset":     [0,0,0,-0.2,-0.2,-0.2,-0.2,-0.2],
                "outmin": 0,
                "outmax": 1
            },
            'LC09_T1L2': {
                "description": 'Fraction of absorbed photosynthetically active radiation',
                "variable": 2,
                "inputBands":      ['cosVZA','cosSZA','cosRAA','SR_B3', 'SR_B4', 'SR_B5', 'SR_B6', 'SR_B7'],
                "inputScaling":     [0.0001,0.0001,0.0001,2.75e-05,2.75e-05,2.75e-05,2.75e-05,2.75e-05],
                "inputOffset":     [0,0,0,-0.2,-0.2,-0.2,-0.2,-0.2],
                "outmin": 0,
                "outmax": 1
            },
            'HLSL30': {
                "description": 'Fraction of absorbed photosynthetically active radiation',
                "variable": 2,
                "inputBands":      ['cosVZA','cosSZA','cosRAA','B3', 'B4', 'B5', 'B6', 'B7'],
                "inputScaling":     [0.0001,.0001,.0001,1,1,1,1,1],
                "inputOffset":     [0,0,0,0,0,0,0,0],
                "outmin": 0,
                "outmax":1
                }
        },
        'fCOVER': {
            "S2_L2A": {
                "description": 'Fraction of canopy cover',
                "variable": 3,
                "inputBands":      ['cosVZA', 'cosSZA', 'cosRAA', 'B03', 'B04', 'B05', 'B06', 'B07', 'B8A', 'B11', 'B12'],
                "inputScaling":    [0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001],
                "inputOffset":     [-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000],
                "outmin": 0,
                "outmax": 1
            },
            "S2_L2A_10m": {
                "description": 'Fraction of canopy cover',
                "variable": 3,
                "inputBands":      ['cosVZA', 'cosSZA', 'cosRAA', 'B02', 'B03', 'B04', 'B08'],
                "inputScaling":    [0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001],
                "inputOffset":     [-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000],
                "outmin": 0,
                "outmax": 1
            },
             'LC08_T1L2': {
                "description": 'Fraction of canopy cover',
                "variable": 3,
                "inputBands":      ['cosVZA','cosSZA','cosRAA','SR_B3', 'SR_B4', 'SR_B5', 'SR_B6', 'SR_B7'],
                "inputScaling":     [0.0001,0.0001,0.0001,2.75e-05,2.75e-05,2.75e-05,2.75e-05,2.75e-05],
                "inputOffset":     [0,0,0,-0.2,-0.2,-0.2,-0.2,-0.2],
                "outmin": 0,
                "outmax": 1
            },
            'LC09_T1L2': {
                "description": 'Fraction of canopy cover',
                "variable": 3,
                "inputBands":      ['cosVZA','cosSZA','cosRAA','SR_B3', 'SR_B4', 'SR_B5', 'SR_B6', 'SR_B7'],
                "inputScaling":     [0.0001,0.0001,0.0001,2.75e-05,2.75e-05,2.75e-05,2.75e-05,2.75e-05],
                "inputOffset":     [0,0,0,-0.2,-0.2,-0.2,-0.2,-0.2],
                "outmin": 0,
                "outmax": 1
            },
            'HLSL30': {
                "description": 'Fraction of canopy cover',
                "variable": 3,
                "inputBands":      ['cosVZA','cosSZA','cosRAA','B3', 'B4', 'B5', 'B6', 'B7'],
                "inputScaling":     [0.0001,.0001,.0001,1,1,1,1,1],
                "inputOffset":     [0,0,0,0,0,0,0,0],
                "outmin": 0,
                "outmax": 1
                }
        },
        'LAI': {
            "S2_L2A": {
                "description": 'Leaf area index',
                "variable": 1,
                "inputBands":      ['cosVZA', 'cosSZA', 'cosRAA', 'B03', 'B04', 'B05', 'B06', 'B07', 'B8A', 'B11', 'B12'],
                "inputScaling":    [0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001],
                "inputOffset":     [-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000],
                "outmin": 0,
                "outmax": 8
            },
            "S2_L2A_10m": {
                "description": 'Leaf area index',
                "variable": 1,
                "inputBands":      ['cosVZA', 'cosSZA', 'cosRAA', 'B02', 'B03', 'B04', 'B08'],
                "inputScaling":    [0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001],
                "inputOffset":     [-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000],
                "outmin": 0,
                "outmax": 8
            },
            'LC08_T1L2': {
                "description": 'Leaf area index',
                "variable": 1,
                "inputBands":      ['cosVZA','cosSZA','cosRAA','SR_B3', 'SR_B4', 'SR_B5', 'SR_B6', 'SR_B7'],
                "inputScaling":     [0.0001,0.0001,0.0001,2.75e-05,2.75e-05,2.75e-05,2.75e-05,2.75e-05],
                "inputOffset":     [0,0,0,-0.2,-0.2,-0.2,-0.2,-0.2],
                "outmin": 0,
                "outmax": 8 
            },
            'LC09_T1L2': {
                "description": 'Leaf area index',
                "variable": 1,
                "inputBands":      ['cosVZA','cosSZA','cosRAA','SR_B3', 'SR_B4', 'SR_B5', 'SR_B6', 'SR_B7'],
                "inputScaling":     [0.0001,0.0001,0.0001,2.75e-05,2.75e-05,2.75e-05,2.75e-05,2.75e-05],
                "inputOffset":     [0,0,0,-0.2,-0.2,-0.2,-0.2,-0.2],
                "outmin": 0,
                "outmax": 8
            },
            'HLSL30': {
                "description": 'Leaf area index',
                "variable": 1,
                "inputBands":      ['cosVZA','cosSZA','cosRAA','B3', 'B4', 'B5', 'B6', 'B7'],
                "inputScaling":     [0.0001,.0001,.0001,1,1,1,1,1],
                "inputOffset":     [0,0,0,0,0,0,0,0],
                "outmin": 0,
                "outmax": 8
                }
        },
        'CCC': {
            "S2_L2A": {
                "description": 'Canopy chlorophyll content',
                "variable": 4,
                "inputBands":      ['cosVZA', 'cosSZA', 'cosRAA', 'B03', 'B04', 'B05', 'B06', 'B07', 'B8A', 'B11', 'B12'],
                "inputScaling":    [0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001],
                "inputOffset":     [-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000],
                "outmin": 0,
                "outmax": 600
            },
            "S2_L2A_10m": {
                "description": 'Canopy chlorophyll content',
                "variable": 4,
                "inputBands":      ['cosVZA', 'cosSZA', 'cosRAA', 'B02', 'B03', 'B04', 'B08'],
                "inputScaling":    [0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001],
                "inputOffset":     [-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000],
                "outmin": 0,
                "outmax": 600
            },
            'LC08_T1L2': {
                "description": 'Canopy chlorophyll content',
                "variable": 4,
                "inputBands":      ['cosVZA','cosSZA','cosRAA','SR_B3', 'SR_B4', 'SR_B5', 'SR_B6', 'SR_B7'],
                "inputScaling":     [0.0001,0.0001,0.0001,2.75e-05,2.75e-05,2.75e-05,2.75e-05,2.75e-05],
                "inputOffset":     [0,0,0,-0.2,-0.2,-0.2,-0.2,-0.2],
                "outmin": 0,
                "outmax": 600
            },
            'LC09_T1L2': {
                "description": 'Canopy chlorophyll content',
                "variable": 4,
                "inputBands":      ['cosVZA','cosSZA','cosRAA','SR_B3', 'SR_B4', 'SR_B5', 'SR_B6', 'SR_B7'],
                "inputScaling":     [0.0001,0.0001,0.0001,2.75e-05,2.75e-05,2.75e-05,2.75e-05,2.75e-05],
                "inputOffset":     [0,0,0,-0.2,-0.2,-0.2,-0.2,-0.2],
                "outmin": 0,
                "outmax": 600
            },
            'HLSL30': {
                "description": 'Canopy chlorophyll content',
                "variable": 4,
                "inputBands":      ['cosVZA','cosSZA','cosRAA','B3', 'B4', 'B5', 'B6', 'B7'],
                "inputScaling":     [0.0001,.0001,.0001,1,1,1,1,1],
                "inputOffset":     [0,0,0,0,0,0,0,0],
                "outmin": 0,
                "outmax": 600
                }
        },
        'CWC': {
            "S2_L2A": {
                "description": 'Canopy water content',
                "variable": 5,
                "inputBands":      ['cosVZA', 'cosSZA', 'cosRAA', 'B03', 'B04', 'B05', 'B06', 'B07', 'B8A', 'B11', 'B12'],
                "inputScaling":    [0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001],
                "inputOffset":     [-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000],
                "outmin": 0,
                "outmax": 0.55
            },
            "S2_L2A_10m": {
                "description": 'Canopy water content',
                "variable": 5,
                "inputBands":      ['cosVZA', 'cosSZA', 'cosRAA', 'B02', 'B03', 'B04', 'B08'],
                "inputScaling":    [0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001],
                "inputOffset":     [-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000],
                "outmin": 0,
                "outmax": 0.55
            },
            'LC08_T1L2': {
                "description": 'Canopy water content',
                "variable": 5,
                "inputBands":      ['cosVZA','cosSZA','cosRAA','SR_B3', 'SR_B4', 'SR_B5', 'SR_B6', 'SR_B7'],
                "inputScaling":     [0.0001,0.0001,0.0001,2.75e-05,2.75e-05,2.75e-05,2.75e-05,2.75e-05],
                "inputOffset":     [0,0,0,-0.2,-0.2,-0.2,-0.2,-0.2],
                "outmin": 0,
                "outmax": 0.55
            },  
            'LC09_T1L2': {
                "description": 'Canopy water content',
                "variable": 5,
                "inputBands":      ['cosVZA','cosSZA','cosRAA','SR_B3', 'SR_B4', 'SR_B5', 'SR_B6', 'SR_B7'],
                "inputScaling":     [0.0001,0.0001,0.0001,2.75e-05,2.75e-05,2.75e-05,2.75e-05,2.75e-05],
                "inputOffset":     [0,0,0,-0.2,-0.2,-0.2,-0.2,-0.2],
                "outmin": 0,
                "outmax":0.55
            }, 
            'HLSL30': {
                "description": 'Canopy water content',
                "variable": 5,
                "inputBands":      ['cosVZA','cosSZA','cosRAA','B3', 'B4', 'B5', 'B6', 'B7'],
                "inputScaling":     [0.0001,.0001,.0001,1,1,1,1,1],
                "inputOffset":     [0,0,0,0,0,0,0,0],
                "outmin": 0,
                "outmax": 0.55
                }
        },
    }
    return(NET_OPTIONS)
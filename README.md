# Welcome to SL2P_PYTHON_package

SL2P-PYTHON_package provides a python implementation of:  
1.  The Simplified Level 2 Product Prototype Processor (SL2P) described in [Weiss and Baret (2016)](https://step.esa.int/docs/extra/ATBD_S2ToolBox_L2B_V1.1.pdf). and
2.  The Canada Centre for Remote Sensing version of SL2P (SL2PCCRS) described in [Fernandes et al. (2024)](https://doi.org/10.1016/j.rse.2024.114060)   
    
It corresponds to algorithms implemented in the [LEAf-Toolbox](https://github.com/rfernand387/LEAF-Toolbox)  

SL2P_PYTHON_package is designed to estimate vegetation biophysical variables (Table 1) from multi-spectral data from different sensors (Table 1). 

Required inputs
---------------
--	The input data collection name (Table 1).  
--  The needed vegetation variable (Table 2).  
-- CSV file containing the needed input bands: examples are provided in [testdata](https://github.com/djamainajib/SL2P_PYTHON_package/tree/main/testdata).  

Input bands depends on:  
--  The input collection (Table 1).  
--  The SL2P version: partition is required as un extra column in the CSV file when SL2PCCRS is used.     

<p align="center"> Table 1: Supported multispectral data sources and the correspending SL2P / SL2PCCRS input bands</p>  

|Collection name                                         |	Description                                              |Input bands |
|----------------------------------------------|-----------------------------------------------------------|-----------------|
|S2_L2A	                 |Sentinel-2 MSI L2A in 20m respatial resolution                               |cosVZA , cosSZA , cosRAA , B03 , B04 , B05 , B06 , B07 , B8A , B11 , B12|
|S2_L2A_10m	 |Sentinel-2 MSI L2A in 10m respatial resolution             |cosVZA , cosSZA , cosRAA , B02 , B03 , B04 , B08|
|LC08_T1L2	               |Landsat-8 L2     |cosVZA , cosSZA , cosRAA , SR_B3 , SR_B4 , SR_B5 , SR_B6 , SR_B7|
|LC09_T1L2               |	Landsat-9 L2|cosVZA , cosSZA , cosRAA , SR_B3 , SR_B4 , SR_B5 , SR_B6 , SR_B7|
|HLSL30|Harmonized Landsat Sentinel-2 |cosVZA , cosSZA , cosRAA , B3 , B4 , B5, B6 , B7|

Processing
----------
SL2P or SL2PCCRS is used to estimate the needed vegetation variable (Table 3) from the input data. 

Please see example provided in [test_package](https://github.com/djamainajib/SL2P_PYTHON_package/blob/main/test_package.ipynb)


Outputs
-------
SL2P_PYTHON_package is designed to estimate five vegetation variables (Table 2). 

Output is a pandas DataFrame with 5 columns (Table 3). 



<p align="center"> Table 2: Vegetation variables supported by SL2P and SL2PCCRS </p>

|Vegetation variable	|Description	|Unit	|Nominal variation range|
|---------------------|-------------|:-----:|:-----------------------:|
|LAI	|Half the total green foliage area per horizontal ground area.	|$m^{2} / m^{2}$ |0 - 8|
|fCOVER	|Fraction of nadir canopy cover	|Ratio	|0 – 1|
|fAPAR	|Fraction of absorbed clear sky PAR at 10:30 am local time	|Ratio	|0 – 1|
|CCC	|Canopy chlorophyll A+B content	|$g / m^{2}$	|0 - 600|
|CWC	|Canopy water content	|$g / m^{2}$	|0 – 1|
|Albedo	|Black sky shortwave albedo at 10:30am local time	|Ratio	|0 – 0.2|

<p align="center"> Table 3: SL2P_PYTHON_package output format (for one needed vegetation variable e.g. LAI) </p>

|Layer                                         |	Description                                              |
|----------------------------------------------|-----------------------------------------------------------|
|estimateLAI	                 |SL2P estimates of LAI                                 | 
|networkID	 |the used netweotk ID to estimate LAI (SL2P: 0, SL2PCCRS: from 1 to depending on the partition)              |
|errorLAI	               |Theoretical estimation error      |
|QC_input               |	0: Valid, 1: inputs out of the domain of the calibration dataset|
|QC_output              |   0: Valid, 1: estimate out of the nominal variation range|



Dependencies:
------------
- rasterio 1.3.9
- matplotlib 3.7.2
- datetime 5.4
- skimage 0.20.0
- tqdm 4.65.0
- scipy 1.11.1
- pickle 0.0.12

How to contribute?
------------
See [CONTRIBUTING.md](https://github.com/djamainajib/SL2P_python/blob/main/CONTRIBUTING.md)


License:
------------
Unless otherwise noted, the source code of this project is covered under Crown Copyright, Government of Canada, and is distributed under the [MIT License](https://github.com/djamainajib/SL2P_python/blob/main/License).

The Canada wordmark and related graphics associated with this distribution are protected under trademark law and copyright law. No permission is granted to use them outside the parameters of the Government of Canada's corporate identity program. For more information, see [Federal identity requirements](https://www.canada.ca/en/treasury-board-secretariat/topics/government-communications/federal-identity-requirements.html).



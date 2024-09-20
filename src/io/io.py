###########################################################
# Scripts for loading an ML model and its training dataset
# Author: monte-flora 
# Email : monte.flora@noaa.gov
###########################################################
# Built-in Python packages
import os
from glob import glob 
from os.path import join
import traceback
import subprocess
import zipfile

# Third party python packages
from joblib import load
import pandas as pd
import numpy as np
import skexplain

# Internal packages
from ..common.calibration_classifier import CalibratedClassifier
from .display_names import PREDICTOR_COLUMNS, TARGET_COLUMN

def unscale_data(X):
    """Unscale the dataset"""
    scaling = { 'wv' : {'mean' : -37.076042, 'std' : 11.884567},
                'ir' : {'mean' : -16.015541, 'std' : 25.805252},
               'vl' : {'mean' : 0.40534842, 'std' : 1.9639382}, 
               'vi' : {'mean' : 0.14749236, 'std' : 0.21128087}
              }
    X_unscaled = X.copy()
    for f in X.columns:
        v = f.split('_')[-1]
        X_unscaled[f] = (X[f] * scaling[v]['std']) + scaling[v]['mean']

    return X_unscaled    


# The data fetching from zenodo can make 10 minutes or more. 
def fetch_zenodo():
    # Fetch the data and models from the Zenodo DOI. 
    print('Fetching data from Zenodo...')
    command = "python -m zenodo_get https://doi.org/10.5281/zenodo.8184201"   
    result = subprocess.run(command, shell=True)
    
    # Path to the ZIP file
    print('Unzipping the files...')
    zip_file_paths = ["models.zip", "datasets.zip"]
    for path in zip_file_paths: 
    
        # Get the directory where the ZIP file is located
        extracted_dir = os.path.dirname(path)

        # Open the ZIP file and extract its contents
        with zipfile.ZipFile(path, 'r') as zip_ref:
            zip_ref.extractall(extracted_dir)

    print('ZIP file extracted successfully.')
    
    # Move all the ML models to a newly created "models" directory. 
    if not os.path.exists("models"):
        os.mkdir ('models')

    subprocess.run("mv *.joblib models/", shell=True)
    subprocess.run("mv *.pkl models/", shell=True)


def load_data_and_model(dataset, dataset_path, model_path, return_groups=False):
    """Load a prefit scikit-learn estimator and its training dataset . 
        
    References
    ------------------
    [1] Handler, S. L., H. D. Reeves, and A. McGovern, 2020: Development of a Probabilistic Subfreezing Road 
            Temperature Nowcast and Forecast Using Machine Learning. Wea. Forecasting, 35, 
            1845–1863, https://doi.org/10.1175/WAF-D-19-0159.1.
    
    [2] 
    
    [3]
    
    
    Parameters
    ------------
    dataset : 'road_surface', 'severe_wind', or 'lightning'
        String identifier of the 3 available datasets/models
        
        'road_surface' : Random forest; inputs described in Handler et al. (2020)[1]
        'lightning' : Neural Network; inputs described in 
        'severe_wind' : Logistic Regression; inputs described in 
    
    dataset_path : path-like
        Parent directory path where the datasets are stored.
    
    model_path : path-like 
        Parent directory path where the ML models are stored.

    return_groups : boolean (default=False) 
        If True, return a dictionary indicating how features are grouped 
        for the grouped feature importance. Used for the grouped
        SAGE computation. 

    Returns
    ------------
        (est_name, model) : 2-tuple of the estimator name and prefit scikit-learn estimator
                            Neccesary input into scikit-explain 
        X : training inputs 
        y : training targets
    """
    if dataset == 'road_surface':
        est_name = 'Random Forest'
        ###calibrator =  load(os.path.join(model_path, 'JTTI_ProbSR_RandomForest_Isotonic.pkl'))
        model = load(os.path.join(model_path,'JTTI_ProbSR_RandomForest.pkl'))
        
        try: 
            train_df = pd.read_csv(os.path.join(dataset_path, 'road_surface_dataset.csv'),)
     
            X = train_df[PREDICTOR_COLUMNS].astype(float)
            y = train_df[TARGET_COLUMN].astype(float).values
        except:
            X,y = skexplain.load_data() 
        
        groups = {'Temperature': ['dwpt2m', 'sfc_temp', 'temp2m', 'hrrr_dT'],
                  
                  'Freezing Duration'  : ['sfcT_hrs_ab_frez', 'sfcT_hrs_bl_frez',  
                                   'date_marker', 'tmp2m_hrs_ab_frez', 'tmp2m_hrs_bl_frez',],
                  
                  'Cloud Coverage' : ['high_cloud', 'low_cloud', 'mid_cloud', 'tot_cloud' ], 
                  
                  'Radiation' : ['gflux', 'lat_hf', 'sat_irbt', 'sens_hf', 'uplwav_flux', 
                                      'vbd_flux', 'vdd_flux', 'd_ground','d_rad_d','d_rad_u']
            }    
            
    elif dataset == 'lightning':
        est_name = 'Neural Network'
        train_df = pd.read_csv(os.path.join(dataset_path, 'lightning_dataset.csv'))
        model = load(os.path.join(model_path,'NN_classification.joblib'))
        features  = [f for f in train_df.columns if 'label' not in f]
        X = train_df[features]
        X = unscale_data(X)
        y = train_df['label_class']
        groups = {'IR' : ['q000_ir', 'q001_ir', 'q010_ir', 'q025_ir', 'q050_ir', 'q075_ir',
                           'q090_ir', 'q099_ir', 'q100_ir',],
                  
                  'WV' : ['q000_wv', 'q001_wv', 'q010_wv',
                          'q025_wv', 'q050_wv', 'q075_wv', 'q090_wv', 'q099_wv', 'q100_wv',],
                  
                  'VIS' : ['q000_vi', 'q001_vi', 'q010_vi', 'q025_vi', 'q050_vi', 'q075_vi',
                           'q090_vi', 'q099_vi', 'q100_vi',],
                  
                  'VIL' : ['q000_vl', 'q001_vl', 'q010_vl',
                           'q025_vl', 'q050_vl', 'q075_vl', 'q090_vl', 'q099_vl', 'q100_vl']
         
         }
        
    elif dataset == 'severe_wind':
        est_name = 'NewLogisticRegression'
        fname = os.path.join(model_path,'LogisticRegression_wind_severe_0km_None_first_hour_realtime.joblib')
        data = load(fname)
        # The training dataset is saved with the model.
        model = data['model']
        X,y = data['X'], data['y']
        
        groups_ = {
                'Near-Surface Winds' : ['ws_80', 'v_10', 'u_10', 'div_10m',],
            
                'Low-level Dynamics' : ['10-500m_bulkshear', 'shear_u_0to1', 'shear_v_0to1',
                                        'srh_0to1', 'srh_0to3',  'uh_0to2_instant',
                                        'w_1km', 'wz_0to2_instant', 
                                 ],
          
          'Reflectivity' : [ 'dbz_1to3', 'dbz_3to5', 'comp_dz'], 
          
          'Thermodynamics' : ['buoyancy', 'cape_sfc', 'cin_sfc', 'lcl_sfc',
                             'low_level_lapse_rate', 'mid_level_lapse_rate', ], 
          
          'Mid-level Dynamics' : ['shear_u_0to6', 'shear_v_0to6', 'uh_2to5_instant', 
                                  'w_up', 'ctt',
                                 ]
          
         }

        unique_names = np.unique([f.split('__')[0] for f in X.columns])
        groups = {n : [] for n in unique_names}
        for f in X.columns:
            groups[f.split('__')[0]].append(f)

    if return_groups:
        return (est_name, model), X, y, groups   
    else:
        return (est_name, model), X, y 
    
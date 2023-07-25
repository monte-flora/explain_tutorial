###########################################################
# Scripts for loading an ML model and its training dataset
# Author: monte-flora 
# Email : monte.flora@noaa.gov
###########################################################

import pandas as pd
import numpy as np
import os
from glob import glob 
from os.path import join
from src.common.calibration_classifier import CalibratedClassifier
from joblib import load
import traceback
from .display_names import PREDICTOR_COLUMNS, TARGET_COLUMN

import sys
sys.path.insert(0, '/home/monte.flora/python_packages/scikit-explain/')
import skexplain

LABELS = {'backward_singlepass' : 'BSP', 
                       'backward_multipass' : 'BMP', 
                       'forward_singlepass' : 'FSP', 
                       'forward_multipass' : 'FMP', 
                       'sobol_total' : 'SBL',
                       'sage' : 'SAGE', 
                       'coefs': 'COEFS', 
                       'shap_sum' : 'SHAP', 
                       'shap' : 'SHAP', 
                       'ale_variance' : 'ALE',
                       'pd_variance' : 'PD', 
                       'ale' : 'ALE',
                       'pd' : 'PD', 
                       'lime' : 'LIME', 
                       'tree_interpreter' : 'TI',
                       'gini' : 'GINI', 
             }


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


def load_data_and_model(dataset, dataset_path, model_path, option='original', 
                        return_dates=False, return_groups=False):
    """Load a X,y of a dataset
    
    Parameters
    ------------
    dataset : 'road_surface', 'tornado', 'severe_hail', 'severe_wind'
    option : 'original', 'reduced'
    dataset_path : path-like
        Base path to the ML dataset dir
    model_path : path-like 
        Base path to the ML model dir

    Returns
    ------------
    model, X, y
    """
    # For this study, we only used the FIRST HOUR dataset from Flora et al. (2021)
    TIME = 'first_hour'
    
    if dataset == 'road_surface':
        est_name = 'Random Forest'
        
        train_df = pd.read_csv(os.path.join(dataset_path, 'probsr_training_data.csv'))
        if option == 'original':
            calibrator =  load(os.path.join(model_path, 'JTTI_ProbSR_RandomForest_Isotonic.pkl'))
            model = load(os.path.join(model_path,'JTTI_ProbSR_RandomForest.pkl'))
            # Just load the RF model so we can use tree interpreter. 
            #model = CalibratedClassifier(rf_orig, calibrator)
            X = train_df[PREDICTOR_COLUMNS].astype(float)
            y = train_df[TARGET_COLUMN].astype(float).values
        else:
            model_name = os.path.join(model_path, f'RandomForest_manualfeatures_12.joblib')
            data = load(model_name)
            model = data['model']
            # Just load the RF model
            ##model = model.base_estimator.named_steps['model']
            X = train_df[data['features']].astype(float)
            y = train_df[TARGET_COLUMN].astype(float).values
            
        groups = {'Temperature': ['dwpt2m', 'sfc_temp', 'temp2m', 'hrrr_dT'],
                  
                  'Freezing Duration'  : ['sfcT_hrs_ab_frez', 'sfcT_hrs_bl_frez',  
                                   'date_marker', 'tmp2m_hrs_ab_frez', 'tmp2m_hrs_bl_frez',],
                  
                  'Cloud Coverage' : ['high_cloud', 'low_cloud', 'mid_cloud', 'tot_cloud' ], 
                  
                  'Radiation' : ['gflux', 'lat_hf', 'sat_irbt', 'sens_hf', 'uplwav_flux', 
                                      'vbd_flux', 'vdd_flux', 'd_ground','d_rad_d','d_rad_u']
            }    
            
    elif dataset == 'lightning':
        est_name = 'Neural Network'
        train_df = pd.read_csv(
            '/home/monte.flora/python_packages/tai4es-trustathon-2022/severe/datasets/lowres_features_train.csv')
        features  = [f for f in train_df.columns if 'label' not in f]
        X = train_df[features]
        X = unscale_data(X)
        y = train_df['label_class']
        model = load('/home/monte.flora/python_packages/tai4es-trustathon-2022/severe/models/NN_classification.joblib')
        
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
        est_name = 'LogisticRegression'
        opt_tag = '' if option == 'original' else 'L1_based_feature_selection_with_manual'
        df = pd.read_feather(os.path.join(dataset_path, 
                             f'original_{TIME}_training_matched_to_{dataset}_0km_data.feather'))
    
        # Load Model
        model_path = os.path.join(model_path,
                                  f'LogisticRegression_first_hour_{dataset}_under_standard_{opt_tag}.pkl')
        data = load(model_path)
        model = data['model']
        X = df[data['features']].astype(float)
        y = df[f'matched_to_{dataset}_0km'].astype(float).values
        dates = df['Run Date'].values
        fti = df['FCST_TIME_IDX'].values
    
    elif dataset == 'new_severe_wind':
        est_name = 'NewLogisticRegression'
        
        data = load(
            '/work/mflora/ML_DATA/NEW_ML_MODELS/LogisticRegression_wind_severe_0km_None_first_hour_realtime.joblib')
        
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

        #groups={}
        #for key, items in groups_.items():
        #    groups[key] = [f for f in X.columns if any(v in f for v in items)]
        
        unique_names = np.unique([f.split('__')[0] for f in X.columns])
        groups = {n : [] for n in unique_names}
        for f in X.columns:
            groups[f.split('__')[0]].append(f)

        
    if return_dates:
        return (est_name, model), X, y, dates, fti
        
    else: 
        if return_groups:
            return (est_name, model), X, y, groups   
        else:
            return (est_name, model), X, y 
    
    
def rename(ds, direction):
    data_vars = [v for v in ds.data_vars if 'pass' in v]
    mapper = {v : f'{direction}_{v}' for v in data_vars}
    
    ds = ds.rename(mapper)
    
    return ds

def load_xai_data(dataset, option='original', adjust_scores=True, kept_all=False,
            basePath = '/work/mflora/explainability_work/new_results',
            all_methods = ['backward_singlepass', 
                           'forward_singlepass', 
                       'backward_multipass', 
                       'forward_multipass', 
                       'sage',  
                       'shap_sum',    
                       'ale_variance',
                       'lime', 
                       'tree_interpreter',
                       'gini', 
                       'coefs', 
                      ]
            ):
    """Loads the XAI output from a given dataset"""
    #'pd_variance' 
    
    methods = all_methods.copy()

    if not kept_all: 
    
        if dataset in ['severe_wind', 'lightning']:
            # Remove the RF-based XAI
            try:
                methods.remove('gini')
                methods.remove('tree_interpreter')
            except:
                pass
        if dataset in ['lightning', 'road_surface']:
            # Remove the LR-based XAI
            try:
                methods.remove('coefs')
            except:
                pass
    if dataset == 'severe_wind':
        name =  'LogisticRegression'
    elif dataset == 'lightning':
        name = 'Neural Network'
    elif dataset == 'new_severe_wind':
        name =  'NewLogisticRegression'
    else:
        name = 'Random Forest'
    
    # Initialize the explainer
    explainer = skexplain.ExplainToolkit()

    filenames = {'backward_singlepass' : join(basePath, f'perm_imp_rank_backward_{dataset}_{option}.nc'), 
                 'backward_multipass' : join(basePath, f'perm_imp_rank_backward_{dataset}_{option}.nc'), 
                 'forward_singlepass' : join(basePath, f'perm_imp_rank_forward_{dataset}_{option}.nc'), 
                 'forward_multipass' : join(basePath, f'perm_imp_rank_forward_{dataset}_{option}.nc'), 
                 'sobol_total' : join(basePath, f'sobol_rank_{dataset}_{option}.nc'), 
                 'sage' : join(basePath, f'sage_rank_{dataset}_{option}.nc'),
                 'coefs': join(basePath, f'coef_rank_{dataset}_{option}.nc'),
                 'shap_sum': join(basePath, f'shap_rank_{dataset}_{option}.nc'),
                 'ale_variance':join(basePath, f'ale_rank_{dataset}_{option}.nc'),
                 'pd_variance':join(basePath, f'pd_rank_{dataset}_{option}.nc'),
                 'lime': join(basePath, f'lime_rank_{dataset}_{option}.nc'),
                 'tree_interpreter': join(basePath, f'ti_rank_{dataset}_{option}.nc'),
                 'gini': join(basePath, f'gini_rank_{dataset}_{option}.nc')
                } 
    results = []
    methods_kept = []
    labels_kept = []
    for method in methods:
        print(f'Loading {method}...') 
        try:
            results.append(explainer.load(filenames[method]))
            methods_kept.append(method)
            labels_kept.append(LABELS[method])
        except Exception as e:
            ###print(traceback.format_exc())
            if kept_all:
                results.append(None)
                methods_kept.append(method)
                labels_kept.append(LABELS[method])
            
            #print(f'{method} did not load!') 

    return results, methods_kept, labels_kept, name  #, feature_names 
    
def to_curve(feature_vals, explain_vals, bins):
    """
    Convert local explainability output to a expected 
    curve like ALE or PD
    Parameters
    -------------------------
        feature (array): input feature values 
        vals (array): explainability output 
        bins (numpy.ndarray): Array of bin edges.

    Returns
    -------------------------
        numpy.ndarray: Mean explainability values as a curve.
    """
    # Separate the explain values into bins and compute the mean value
    # in each bin.
    inds = np.digitize(feature_vals, bins=bins) - 1
    mean_explain_vals = np.array([np.mean(explain_vals[inds == i]) for i in range(len(bins)+1)])
    mean_explain_vals = 0.5 * (mean_explain_vals[:-1] + mean_explain_vals[1:])

    return mean_explain_vals

def to_dataset(local_ds, method, ale):

    X = local_ds['X']
    est_name = list(local_ds.data_vars)[0].split('__')[-1]
    X = pd.DataFrame(X, columns=local_ds.attrs['features'])
    vals = pd.DataFrame(local_ds[f'{method}_values__{est_name}'].values, columns=X.columns)

    dataset = {}
    for f in X.columns:
        feature_vals = X[f]
        explain_vals = vals[f]
        bins = ale[f'{f}__bin_values'].values
        curve = to_curve(feature_vals, explain_vals, bins)
        dataset[f'{f}__{est_name}__{method}'] = (['n_bootstrap', f'n_bins__{f}'], [curve])
        dataset[f'{f}__bin_values'] = ([f'n_bins__{f}'], bins)
    
    return xr.Dataset(dataset)

def load_xai_curves(dataset, option='original', basePath = '/work/mflora/explainability_work/new_results',):
    TO_CURVES = ['shap']#, 'lime', 'tree_interpreter']
    
    filenames = { 
                 'shap': join(basePath, f'shap_{dataset}_{option}.nc'),
                 'ale':join(basePath, f'ale_{dataset}_{option}.nc'),
                 'pd':join(basePath, f'pd_{dataset}_{option}.nc'),
                 'lime': join(basePath, f'lime_{dataset}_{option}.nc'),
                 'tree_interpreter': join(basePath, f'ti_{dataset}_{option}.nc'),
                } 
    
    explainer = skexplain.ExplainToolkit()
    ale = explainer.load(filenames['ale'])
    #pd = explainer.load(filenames['pd'])
    
    results = [ale]#, pd]
    methods_kept = ['ale']#, 'pd']
    labels_kept = ['ALE']#, 'PD'] 
    
    for method in TO_CURVES:
        try:
            data = explainer.load(filenames[method])
            dataset = to_dataset(data, method, ale)

            methods_kept.append(method)
            results.append(dataset)
            labels_kept.append(LABELS[method])
        except:
            continue
    
    return results, methods_kept, labels_kept
   

def load_grouped_xai_data(dataset, option='original', adjust_scores=True, kept_all=False,
            basePath = '/work/mflora/explainability_work/new_results',
            all_methods = [
                       'sage',  
                       'shap_sum',    
                       'ale_variance',
                       'lime', 
                       'tree_interpreter',
                       'gini', 
                       'coefs', 
                      ]
            ):
    """Loads the Grouped XAI output from a given dataset"""
    
    methods = all_methods.copy()

    if not kept_all: 
        if dataset in ['severe_wind', 'lightning']:
            # Remove the RF-based XAI
            try:
                methods.remove('gini')
                methods.remove('tree_interpreter')
            except:
                pass
        if dataset in ['lightning', 'road_surface']:
            # Remove the LR-based XAI
            try:
                methods.remove('coefs')
            except:
                pass
            
    if dataset == 'severe_wind':
        name =  'LogisticRegression'
    elif dataset == 'lightning':
        name = 'Neural Network'
    elif dataset == 'new_severe_wind':
        name =  'NewLogisticRegression'
    else:
        name = 'Random Forest'
    
    # Initialize the explainer
    explainer = skexplain.ExplainToolkit()

    filenames = {
                 'sage' : join(basePath, f'grouped_sage_rank_{dataset}_{option}.nc'),
                 'coefs': join(basePath, f'coef_{dataset}_{option}.nc'),
                 'shap_sum': join(basePath, f'shap_{dataset}_{option}.nc'),
                 'ale':join(basePath, f'ale_{dataset}_{option}.nc'),
                 'pd':join(basePath, f'pd_{dataset}_{option}.nc'),
                 'lime': join(basePath, f'lime_{dataset}_{option}.nc'),
                 'tree_interpreter': join(basePath, f'ti_{dataset}_{option}.nc'),
                 'gini': join(basePath, f'gini_rank_{dataset}_{option}.nc')
                } 
    results = []
    methods_kept = []
    labels_kept = []
    for method in methods:
        print(f'Loading {method}...') 
        try:
            results.append(explainer.load(filenames[method]))
            methods_kept.append(method)
            labels_kept.append(LABELS[method])
        except Exception as e:
            ###print(traceback.format_exc())
            if kept_all:
                results.append(None)
                methods_kept.append(method)
                labels_kept.append(LABELS[method])
            
            #print(f'{method} did not load!') 

    return results, methods_kept, labels_kept, name  #, feature_names 
    
    
import xarray as xr
def to_xarray(shap_data, estimator_name, feature_names=None):
    dataset={}
    
    shap_values = shap_data['shap_values']
    bias = shap_data['bias']
    
    dataset[f'shap_values__{estimator_name}'] = (['n_examples', 'n_features'], shap_values)
    dataset[f'bias__{estimator_name}'] = (['n_examples'], bias.astype(np.float64))
    dataset['X'] = (['n_examples', 'n_features'], shap_data['X'])
    dataset['y'] = (['n_examples'], shap_data['targets'])
    
    ds = xr.Dataset(dataset)
    #ds.attrs['features'] = feature_names
    
    return ds 
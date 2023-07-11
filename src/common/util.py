import numpy as np
import sage

def to_grouped_importance(dataset, method):

    est_name = list(dataset.data_vars)[0].split('__')[-1]
    vals = dataset[f'{method}_values__{est_name}'].values
    features = list(dataset.attrs['features'])

    group_val = np.zeros(len(groups.keys()))
    names = []
    for i, (name, group) in enumerate(groups.items()):
        inds = [features.index(f) for f in group]
    
        group_val[i] = np.sum(vals[:,inds])
        names.append(name)
    
    results = to_skexplain_importance(group_val, 
                                 estimator_name = est_name,
                                 feature_names = names,
                                  method = f'grouped_{method}',
                                  normalize=False
                                 )
    
    return results 


# Create a subsample of the data 
def subsampler(X, y, size=None, feature=None, thres=None):
    try:
        y=y.values
    except:
        y=y
    if size is not None:
        rs = np.random.RandomState(123)
        inds = rs.choice(len(X), size=size, replace=False)
    elif feature is not None:
        inds = np.where(X[feature]>thres)[0]
    
    X_sub = X.iloc[inds, :]
    y_sub = y[inds]

    X_sub.reset_index(drop=True, inplace=True)
    
    return X_sub, y_sub

def normalize_importance(scores):
    """Min-max normalization of importance scores"""
    return scores / (np.percentile(scores, 99) - np.percentile(scores, 1))

# Compute SAGE
def compute_sage(model, X, y, background, groups=None, n_jobs=1):
    """Compute SAGE"""
    # Set up an imputer to handle missing features
    random_state = np.random.RandomState(42)
    random_inds = np.random.choice(len(background), size=50, replace=False)
    try:
        X_rand = background.values[random_inds,:]
    except:
        X_rand = background[random_inds,:]
    
    # Set up the imputer. 
    if hasattr(model, 'predict_proba'):
        model_ = model.predict_proba
        loss = 'cross entropy'
    else:
        model_ = model.predict
        loss = 'mse'
    
    if groups is None:
        imputer = sage.MarginalImputer(model_, X_rand)
    else:
        imputer = sage.GroupedMarginalImputer(model_, X_rand, groups)

    # Set up an estimator. 
    estimator = sage.PermutationEstimator(imputer, loss, n_jobs=n_jobs)

    sage_values = estimator(X, y)
    
    return sage_values
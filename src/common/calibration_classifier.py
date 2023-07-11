from sklearn.base import (BaseEstimator, ClassifierMixin, RegressorMixin, clone,
                   MetaEstimatorMixin)

from sklearn.utils.validation import check_is_fitted
from sklearn.utils import check_X_y, check_array
import numpy as np

class CalibratedClassifier(BaseEstimator, ClassifierMixin,
                             MetaEstimatorMixin):

    def __init__(self, base_estimator, calibrator):
        self.base_estimator_ = base_estimator
        self.calibrator_ = calibrator

    def fit(self, X, y):
        pass

    def predict(self, X):
        pass

    def score(self, X,y):
        pass

    def predict_proba(self,X):
        check_is_fitted(self.base_estimator_)
        check_is_fitted(self.calibrator_)
        X = check_array(X, accept_sparse=['csc', 'csr', 'coo'],
                        force_all_finite=False)

        n_classes = 2
        proba = np.zeros((X.shape[0], n_classes))

        probabilities = self.base_estimator_.predict_proba(X)[:,1]

        proba[:, 1] = self.calibrator_.predict(probabilities)

        proba[:, 0] = 1. - proba[:, 1]

        # XXX : for some reason all probas can be 0
        proba[np.isnan(proba)] = 1. / n_classes

        # Deal with cases where the predicted probability minimally exceeds 1.0
        proba[(1.0 < proba) & (proba <= 1.0 + 1e-5)] = 1.0

        return proba
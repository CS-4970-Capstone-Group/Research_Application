import pytest
import numpy as np
import heart_risk_classifier

def risk_class_good_input():
    hc = heart_risk_classifier.Heart_Risk_Classifier
    test_arr = np.random.rand(1,3000)
    test_arr = np.expand_dims(test_arr, axis=2)
    assert hc.classify_risk("model.h5",test_arr) > 0

def risk_class_bad_input():
    hc = heart_risk_classifier.Heart_Risk_Classifier
    test_arr = np.random.rand(1,4000)
    test_arr = np.expand_dims(test_arr, axis=2)
    assert hc.classify_risk("model.h5",test_arr) == -1
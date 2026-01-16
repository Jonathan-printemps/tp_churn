import os
import pytest
import joblib
from sklearn.linear_model import LogisticRegression
import numpy as np


class TestChurnModel:
    """Tests for the churn model"""
    
    @pytest.fixture(scope="class")
    def model_path(self):
        """Define the path to the model file"""
        return "data/churn_model_clean.pkl"
    
    def test_model_file_exists(self, model_path):
        """Test that the model file exists"""
        assert os.path.exists(model_path), f"Model file {model_path} does not exist"
    
    def test_model_is_logistic_regression(self, model_path):
        """Test that the loaded model is a LogisticRegression instance"""
        model = joblib.load(model_path)
        assert isinstance(model, LogisticRegression), "Model is not a LogisticRegression instance"
    
    def test_model_returns_prediction(self, model_path):
        """Test that the model can make predictions"""
        model = joblib.load(model_path)
        
        # Create a sample input (Age, Account_Manager, Years, Num_Sites)
        X_sample = np.array([[30, 1, 5, 2]])
        
        # Make prediction
        prediction = model.predict(X_sample)
        
        # Check that prediction is not empty and is a valid output
        assert prediction is not None, "Model returned None"
        assert len(prediction) > 0, "Model returned empty prediction"
        assert prediction[0] in [0, 1], "Prediction is not a valid binary classification (0 or 1)"
    
    def test_model_returns_prediction_proba(self, model_path):
        """Test that the model can return prediction probabilities"""
        model = joblib.load(model_path)
        
        # Create a sample input
        X_sample = np.array([[30, 1, 5, 2]])
        
        # Get prediction probabilities
        proba = model.predict_proba(X_sample)
        
        # Check that probabilities are valid
        assert proba is not None, "Model returned None for predict_proba"
        assert len(proba) > 0, "Model returned empty probabilities"
        assert proba.shape[1] == 2, "Probabilities should have 2 classes"
        assert np.allclose(proba[0].sum(), 1.0), "Probabilities should sum to 1"

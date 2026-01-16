import pytest
import sys
import os
from pathlib import Path

# Add the parent directory to the path to import app
sys.path.insert(0, str(Path(__file__).parent.parent))

from app import app


class TestFlaskApp:
    """Tests for the Flask application"""
    
    @pytest.fixture
    def client(self):
        """Create a test client for the Flask app"""
        app.config['TESTING'] = True
        with app.test_client() as client:
            yield client
    
    def test_app_exists(self):
        """Test that the Flask app is created"""
        assert app is not None
        assert app.name == '__main__' or app.name == 'app'
    
    def test_home_route_exists(self, client):
        """Test that the home route exists and returns 200"""
        response = client.get('/')
        assert response.status_code == 200
    
    def test_home_route_returns_html(self, client):
        """Test that the home route returns HTML content"""
        response = client.get('/')
        assert response.status_code == 200
        assert response.content_type.startswith('text/html')
    
    def test_predict_route_exists(self, client):
        """Test that the predict route exists"""
        # POST to /predict with required data
        data = {
            'Age': '30',
            'Account_Manager': '1',
            'Years': '5',
            'Num_Sites': '2'
        }
        response = client.post('/predict', data=data)
        # Should return 200 if successful or valid JSON error
        assert response.status_code == 200
    
    def test_predict_with_valid_data(self, client):
        """Test prediction with valid data"""
        data = {
            'Age': '30',
            'Account_Manager': '1',
            'Years': '5',
            'Num_Sites': '2'
        }
        response = client.post('/predict', data=data)
        
        assert response.status_code == 200
        assert response.content_type == 'application/json'
        
        json_data = response.get_json()
        assert json_data is not None
        assert 'churn_prediction' in json_data
        assert json_data['churn_prediction'] in [0, 1]
    
    def test_predict_with_different_ages(self, client):
        """Test prediction with various ages"""
        test_cases = [
            ('20', '0', '2', '1'),
            ('50', '1', '10', '5'),
            ('35', '1', '7', '3'),
        ]
        
        for age, manager, years, sites in test_cases:
            data = {
                'Age': age,
                'Account_Manager': manager,
                'Years': years,
                'Num_Sites': sites
            }
            response = client.post('/predict', data=data)
            
            assert response.status_code == 200
            json_data = response.get_json()
            assert 'churn_prediction' in json_data
            assert json_data['churn_prediction'] in [0, 1]
    
    def test_predict_missing_age(self, client):
        """Test prediction with missing Age parameter"""
        data = {
            'Account_Manager': '1',
            'Years': '5',
            'Num_Sites': '2'
        }
        response = client.post('/predict', data=data)
        
        assert response.status_code == 200
        json_data = response.get_json()
        assert 'error' in json_data
    
    def test_predict_missing_account_manager(self, client):
        """Test prediction with missing Account_Manager parameter"""
        data = {
            'Age': '30',
            'Years': '5',
            'Num_Sites': '2'
        }
        response = client.post('/predict', data=data)
        
        assert response.status_code == 200
        json_data = response.get_json()
        assert 'error' in json_data
    
    def test_predict_missing_years(self, client):
        """Test prediction with missing Years parameter"""
        data = {
            'Age': '30',
            'Account_Manager': '1',
            'Num_Sites': '2'
        }
        response = client.post('/predict', data=data)
        
        assert response.status_code == 200
        json_data = response.get_json()
        assert 'error' in json_data
    
    def test_predict_missing_num_sites(self, client):
        """Test prediction with missing Num_Sites parameter"""
        data = {
            'Age': '30',
            'Account_Manager': '1',
            'Years': '5'
        }
        response = client.post('/predict', data=data)
        
        assert response.status_code == 200
        json_data = response.get_json()
        assert 'error' in json_data
    
    def test_predict_invalid_age(self, client):
        """Test prediction with invalid Age (non-numeric)"""
        data = {
            'Age': 'invalid',
            'Account_Manager': '1',
            'Years': '5',
            'Num_Sites': '2'
        }
        response = client.post('/predict', data=data)
        
        assert response.status_code == 200
        json_data = response.get_json()
        assert 'error' in json_data
    
    def test_predict_invalid_account_manager(self, client):
        """Test prediction with invalid Account_Manager (non-integer)"""
        data = {
            'Age': '30',
            'Account_Manager': 'invalid',
            'Years': '5',
            'Num_Sites': '2'
        }
        response = client.post('/predict', data=data)
        
        assert response.status_code == 200
        json_data = response.get_json()
        assert 'error' in json_data
    
    def test_predict_returns_json(self, client):
        """Test that predict returns valid JSON"""
        data = {
            'Age': '30',
            'Account_Manager': '1',
            'Years': '5',
            'Num_Sites': '2'
        }
        response = client.post('/predict', data=data)
        
        assert response.content_type == 'application/json'
        json_data = response.get_json()
        assert json_data is not None
    
    def test_predict_with_boundary_values(self, client):
        """Test prediction with boundary values"""
        data = {
            'Age': '18',
            'Account_Manager': '0',
            'Years': '0',
            'Num_Sites': '1'
        }
        response = client.post('/predict', data=data)
        
        assert response.status_code == 200
        json_data = response.get_json()
        assert 'churn_prediction' in json_data
        assert json_data['churn_prediction'] in [0, 1]
    
    def test_predict_with_high_values(self, client):
        """Test prediction with high values"""
        data = {
            'Age': '100',
            'Account_Manager': '1',
            'Years': '50',
            'Num_Sites': '100'
        }
        response = client.post('/predict', data=data)
        
        assert response.status_code == 200
        json_data = response.get_json()
        assert 'churn_prediction' in json_data
        assert json_data['churn_prediction'] in [0, 1]
    
    def test_home_route_get_only(self, client):
        """Test that home route only accepts GET"""
        response = client.post('/')
        # Flask returns 405 for Method Not Allowed
        assert response.status_code == 405
    
    def test_predict_get_not_allowed(self, client):
        """Test that predict route does not accept GET"""
        response = client.get('/predict')
        # Flask returns 405 for Method Not Allowed
        assert response.status_code == 405

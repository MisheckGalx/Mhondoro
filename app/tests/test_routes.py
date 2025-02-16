import unittest
from app import create_app, db
from app.models import User, Equipment

class BaseTestCase(unittest.TestCase):
    """Base test case for setting up and tearing down the testing environment."""
    
    def setUp(self):
        """Setup the test client and configure the app for testing."""
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Use an in-memory SQLite DB for testing
        db.create_all()  # Create all database tables
    
    def tearDown(self):
        """Clean up after each test."""
        db.session.remove()
        db.drop_all()

class TestEquipmentAPI(BaseTestCase):
    """Test case for testing the Equipment API."""
    
    def test_get_equipments(self):
        """Test the retrieval of equipment data."""
        response = self.client.get('/equipments')
        self.assertEqual(response.status_code, 200)  # Ensure the status code is 200 (OK)

class TestUserAPI(BaseTestCase):
    """Test case for testing the User API."""
    
    def test_register_user(self):
        """Test the user registration functionality."""
        response = self.client.post('/register', json={
            'username': 'testuser',
            'password': 'password123',
            'email': 'testuser@example.com'
        })
        self.assertEqual(response.status_code, 201)  # Ensure the status code is 201 (Created)
        self.assertIn('testuser', response.get_json()['username'])  # Ensure the username is in the response

if __name__ == '__main__':
    unittest.main()

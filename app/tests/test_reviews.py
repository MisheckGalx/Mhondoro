import unittest
from app import app, db
from models import Review

class ReviewTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.user_token = "your_test_jwt_token"

    def test_add_review(self):
        response = self.client.post(
            "/api/reviews/",
            json={"supplier_id": 2, "rating": 5, "comment": "Great service!"},
            headers={"Authorization": f"Bearer {self.user_token}"}
        )
        self.assertEqual(response.status_code, 201)

import unittest
from app import app, db
from models import Inquiry

class InquiryTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.user_token = "your_test_jwt_token"

    def test_send_inquiry(self):
        response = self.client.post(
            "/api/inquiries/",
            json={"supplier_id": 2, "equipment_id": 5, "message": "Is this available?"},
            headers={"Authorization": f"Bearer {self.user_token}"}
        )
        self.assertEqual(response.status_code, 201)

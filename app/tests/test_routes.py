import unittest
from app import create_app, db
from app.models import Equipment

class EquipmentTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app().test_client()

    def test_get_equipments(self):
        response = self.app.get('/equipments')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()

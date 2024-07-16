import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_hello_world(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello World', response.data)
        self.assertIn(b'[Your Name]', response.data)

if __name__ == '__main__':
    unittest.main()
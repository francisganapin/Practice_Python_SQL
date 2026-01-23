import unittest
from app import app



class FlaskTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello, Flask!', response.data)

    def test_about(self):
        response = self.app.get('/about')
        self.assertEqual(response.status_code,200)
        self.assertIn(b'This is about Page',response.data)

    def test_multiply(self):
        response = self.app.get('/multiply/6/7')
        self.assertEqual(response.status_code,200)
        self.assertIn(b'42',response.data)

if __name__ == '__main__':
    unittest.main()
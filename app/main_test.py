from app import app
import unittest

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        result = self.app.get('/')

        self.assertEqual(result.status_code, 200)

    def test_about(self):
        result = self.app.get('/about')

        self.assertEqual(result.status_code, 200)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()

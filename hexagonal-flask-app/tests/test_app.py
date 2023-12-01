import unittest
from flask import Flask
from app.main import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True 

    def test_home_status_code(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_data(self):
        response = self.app.get('/')
        self.assertTrue(b'Welcome to Hexagonal Architecture Flask App' in response.data)

if __name__ == "__main__":
    unittest.main()
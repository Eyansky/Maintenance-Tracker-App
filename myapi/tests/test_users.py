"""
Main Test  for users
"""

import json
import unittest
from myapi.api import app


class TestUsers(unittest.TestCase):
    """
        Test Users
    """

    def setUp(self):
        """code that is executed before each test"""
        app.testing = True
        self.app = app.test_client()
        self.data = {
            "firstname":"Ian",
            "lastname":"Mwangi",
            "email":"ian@eyansky.com",
            "username": "eyansky",
            "password": "qwerty"
        }

        self.error_data = {
            "firstname":"mwangi",
            "lastname":"wairimu",
            "email":"mwangi@mwangi.com",
            "username": "mwangi",
            "password": "x"
        }

    def test_register(self):
        """Test for successful registration"""
        response = self.app.post('/api/v1/users/register',
                                 data=json.dumps(self.data),
                                 content_type="application/json")
        result = json.loads(response.data)
        self.assertEqual(result["status"], "ok")
        self.assertEqual(response.status_code, 201)

    def test_invalidemail(self):
        """Test for invalid email"""
        response = self.app.post('/api/v1/users/register',
                                 data=json.dumps(self.data),
                                 content_type="application/json")
        result = json.loads(response.data)
        self.assertEqual(result["status"], "wrong")
        self.assertEqual(response.status_code, 400)
    
    def test_emailexist(self):
        """
        Test if email exists
        """
        response = self.app.post('/api/v1/users/register',
                                 data=json.dumps(self.data),
                                 content_type="application/json")
        result = json.loads(response.data)
        self.assertEqual(result["status"], "wrong")
        self.assertEqual(response.status_code, 201)


if __name__ == "__main__":
    unittest.main()
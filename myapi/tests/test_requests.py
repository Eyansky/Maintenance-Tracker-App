"""
Main Test  for Requests
"""

import json
import unittest
from flask_jwt_extended import (create_access_token)

from myapi.api import app


class TestRequests(unittest.TestCase):
    """
        Test add Requests
    """

    def setUp(self):
        """
        code that is executed before each test
        """
        app.testing = True
        self.app = app.test_client()
        self.user = {
            "firstname": "wairimu",
            "lastname": "wairimu",
            "email": "another@mail.com",
            "username": "iwairimu",
            "password": "wairimu"
        }
        self.login_user = {
            "username": "iwairimu",
            "password": "wairimu"
        }
        self.register = self.app.post(
            '/api/v1/users/register',
            data=json.dumps(self.user),
            content_type='application/json'
        )
        self.login = self.app.post(
            '/api/v1/users/login',
            data=json.dumps(self.login_user),
            content_type='application/json'
        )
        self.data = json.loads(self.login.data.decode())
        self.token = self.data["auth_token"]

        self.request = {
            "title": "eyansky",
            "request": "Eyansky is my name. I enjoy every bit of it."
        }

    def test_requests(self):
        """
        Test for successful request
        """
        headers = {
            'Authorization': 'Bearer {}'.format(self.token)
        }
        response = self.app.post(
            '/api/v1/users/requests',
            data=json.dumps(self.request),
            content_type='application/json',
            headers=headers
        )
        result = json.loads(response.data.decode())
        self.assertEqual(result["status"], "ok")
        self.assertEqual(response.status_code, 201)

    def test_view_all_requests(self):
        """
        Test for view all requests
        """

        headers = {
            'Authorization': 'Bearer {}'.format(self.token)
        }
        response = self.app.get(
            '/api/v1/users/requests',
            headers=headers
        )
        self.assertEqual(response.status_code, 200)

    def test_get_single_request(self):
        """
        Test for view one request
        """
        headers = {
            'Authorization': 'Bearer {}'.format(self.token)
        }
        self.app.post(
            '/api/v1/users/requests',
            data=json.dumps(self.request),
            content_type='application/json',
            headers=headers
        )

        response = self.app.get(
            '/api/v1/users/requests/1',
            headers=headers
        )
        self.assertEqual(response.status_code, 200)

    def test_get_single_request_fail(self):
        """
        Test for view one request fail
        """

        headers = {
            'Authorization': 'Bearer {}'.format(self.token)
        }
        response = self.app.get(
            '/api/v1/users/requests/123233',
            headers=headers
        )
        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()

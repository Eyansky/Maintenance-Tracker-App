"""
Main Test  for Requests
"""

import json
import unittest
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
        self.request = {
            "title": "eyansky",
            "request": "Eyansky is my name. I enjoy every bit of it."
        }

    def test_requests(self):
        """
        Test for successful request
        """
        response = self.app.post('api/v1/users/requests',
                                 data=json.dumps(self.request),
                                 content_type="application/json")
        result = json.loads(response.data)
        self.assertEqual(result["status"], "ok")
        self.assertEqual(response.status_code, 201)
    
    def test_view_all_requests(self):
        """
        Test for view all requests
        """
        response = self.app.get('api/v1/users/requests',
                                data=json.dumps(self.request),
                                content_type="application/json")
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()


import unittest
import json
from maintenance-tracker.api import app


class MainTests(unittest.TestCase):
   
    url_prefix = '/api/v1/'

    def setUp(self):
        """
            Set up test data
        """
        self.app = app.test_client()
        self.app.testing = True

        

        self.sample_user = {
            'username': 'eyansky',
            'email': 'eyansky@ian.com',
            'password': 'qwerty',
            'confirm_password': 'qwerty'
        }
        self.exist_user = {
            'username': 'ian',
            'email': 'ian@ian.com',
            'password': 'qwerty',
            'confirm_password': 'qwerty'
        }

        self.exist_admin = {
            'username': 'admin',
            'email': 'admin@admin.com',
            'password': 'root',
            'confirm_password': 'root'
        }
        
        save_user = User()
        save_user.save({
            'username': self.sample_user['username'],
            'email': self.sample_user['email'],
            'password': self.sample_user['password'],
            'confirm_password': self.sample_user['confirm_password']
        })
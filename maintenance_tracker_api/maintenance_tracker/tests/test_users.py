"""
    User test Class
"""
import unittest
import json
from maintenance_tracker.api import app
from tests.test_api import MainTests


class UserTests(MainTests):

    def test_registration(self):
        '''
            Testing registration
        '''
        response = self.app.post(self.url_prefix + 'auth/register', data=json.dumps({
            'username': self.exist_user['username'],
            'email': self.exist_user['email'],
            'password': self.exist_user['password'],
            'confirm_password': self.exist_user['confirm_password']
        }), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn(b'have been successfully registered', response.data)

    def test_exist_email(self):
        '''
            Testing registration with existing email
        '''
        response = self.app.post(self.url_prefix + 'auth/register', data=json.dumps({
            'username': self.exist_user['username'],
            'email': self.exist_user['email'],
            'password': self.exist_user['password'],
            'confirm_password': self.exist_user['confirm_password']
        }), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'Sorry the email address has been taken', response.data)

    def test_wrong_registration(self):
        """
            Test registration with incomplete data
        """
        response = self.app.post(self.url_prefix + 'auth/register', data=json.dumps({
            'username': 'dummy name',
            'confirm_password': self.exist_user['confirm_password']
        }), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'Please provide', response.data)

    def test_login(self):
        """
            Testing login
        """
        response = self.app.post(self.url_prefix + 'auth/login', data=json.dumps({
            'email': self.sample_user['email'],
            'password': self.sample_user['password']
        }), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'successfully logged', response.data)

    def test_invalid_password(self):
        """
            Testing for invalid password
        """
        response = self.app.post(self.url_prefix + 'auth/login', data=json.dumps({
            'email': self.sample_user['email'],
            'password': 'anyinvalidpassword'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 401)
        self.assertIn(b'Invalid password', response.data)

    def test_invalid_credentials(self):
        """
            Testing for invalid credentials
        """
        response = self.app.post(self.url_prefix + 'auth/login', data=json.dumps({
            'email': 'anyemail',
            'password': 'anyinvalidpassword'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 401)
        self.assertIn(b'Invalid email or password', response.data)

    def test_incomplete_creds(self):
        """
            Test registration with incomplete data
        """
        response = self.app.post(self.url_prefix + 'auth/login', data=json.dumps({
            'email': 'dummy@dummy.com',
        }), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'Please provide', response.data)

    def test_logout(self):
        """
            Test Logout
        """
        response = self.app.post(self.url_prefix + 'auth/logout',
                                 data={}, headers={'Authorization': self.test_token})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'You have successfully logged out', response.data)

    def test_password_reset(self):
        """
            Testing password Reset
        """
        response = self.app.post(self.url_prefix + 'auth/reset-password', data=json.dumps({
            'old_password': self.sample_user['password'],  # Old password
            'new_password': 'abcd',
        }), content_type='application/json',
            headers={'Authorization': self.test_token})
        self.assertEqual(response.status_code, 201)
        self.assertIn(
            b'You have successfully changed your password', response.data)

    def test_invalid_old_password_reset(self):
        """
            Testing password Reset with invalid old password
        """
        response = self.app.post(self.url_prefix + 'auth/reset-password', data=json.dumps({
            'old_password': 'xxxxxxxx',  # Invalid Old password
            'new_password': 'abcd',
        }), content_type='application/json',
            headers={'Authorization': self.test_token})
        self.assertEqual(response.status_code, 400)
        self.assertIn(
            b'Invalid old password', response.data)

    def test_invalid_data_password_reset(self):
        """
            Testing password Reset with invalid details
        """
        response = self.app.post(self.url_prefix + 'auth/reset-password', data=json.dumps({
            'new_password': '123456',
        }), content_type='application/json',
            headers={'Authorization': self.test_token})
        self.assertEqual(response.status_code, 400)
        self.assertIn(
            b'Please provide valid details', response.data)

    def test_validation_methods(self):
        '''
            Test validation methods (same,minimum,email,string)
        '''
        response = self.app.post(self.url_prefix + 'auth/register', data=json.dumps({
            'username': '@@@',
            'email': 'sdfsd@dfg',
            'password': '123',
            'confirm_password': '123456789'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'Invalid email address', response.data)
        self.assertIn(b'should be string', response.data)
        self.assertIn(b'don\'t match', response.data)
        self.assertIn(b'should not be less', response.data)

if __name__ == "__main__":
    unittest.main()
"""
Users endpoint
"""
from flask_restful import Resource
from flask import request
from myapi.api.database.models import add_user, login, add_request
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity, get_jwt_claims)


class UserRegister(Resource):
    """
    Register a new user.
    """

    def is_valid(self, item):
        """
            checking for valid credentials
        """
        errors = {}
        if not item.get("firstname"):
            errors['firstname'] = "First name is required"

        if not item.get("lastname"):
            errors['lastname'] = "Last name is required"

        if not item.get("username"):
            errors['username'] = "Username is required"
        elif len(item.get("username")) < 5:
            errors["username"] = "username must be more than five characters"

        if not item.get("password"):
            errors["password"] = "Password is required"
        elif len(item.get("password")) < 7:
            errors["password"] = "Password must be more than seven characters"

        return len(errors) == 0, errors

    def post(self):
        if request.is_json:
            valid, errors = self.is_valid(request.json)
            if not valid:
                return {"data": errors, "status": "error"}, 400
            # create user
            result = request.json
            firstname = result['firstname']
            lastname = result['lastname']
            username = result['username']
            role = "user"
            password = result['password']

            user = {
                "firstname": firstname,
                "lastname": lastname,
                "username": username,
                "role": role,
                "password": password}
            # add to database
            add_user(user)

            return {"status": "ok", "auth": "User Has beeen created"}, 201
        else:
            return {"message": "Request should be in JSON",
                    "status": "error"}, 400


class UserLogin(Resource):
    """
    Login a new user.
    """

    def is_valid(self, item):
        """
            checking for valid credentials
        """
        errors = {}
        if not item.get("username"):
            errors['username'] = "Username is required"
        elif len(item.get("username")) < 5:
            errors["username"] = "username must be more than five characters"

        if not item.get("password"):
            errors["password"] = "Password is required"
        elif len(item.get("password")) < 7:
            errors["password"] = "Password must be more than seven characters"

        return len(errors) == 0, errors

    def post(self):
        if request.is_json:
            valid, errors = self.is_valid(request.json)
            if not valid:
                return {"data": errors, "status": "error"}, 400
            # user details
            result = request.json
            username = result['username']
            password = result['password']

            # from database
            details = login(username)
            if details is None:
                response = {
                    "status": "not found",
                    "message": "User has not been Registered"
                }
                return response, 404
            elif details[4] != password:
                response = {
                    "status": "Failed Dependency",
                    "message": "wrong password"
                }
                return response, 424
            elif details[4] == password:
                username = details[2]
                access_token = create_access_token(identity=username)
                response = {
                    "status": "accepted",
                    "message": access_token
                }
                return response, 202


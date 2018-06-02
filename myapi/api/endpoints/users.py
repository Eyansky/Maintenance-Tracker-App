from flask_restful import Resource
from flask_restful import reqparse
from myapi.api.resources.serializers import user_serializer
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)


from myapi.api.resources.models import add_user, view_users, login


class User_Register(Resource):
    """
    Register a new user.
    """

    def get(self):
        return (view_users()), 200

    def post(self):
        """ Add a user """
        parser = reqparse.RequestParser()
        parser.add_argument("firstname",
                            required=True,
                            help="Enter first name")
        parser.add_argument("lastname",
                            required=True,
                            help="Enter last name")
        parser.add_argument("username",
                            required=True,
                            help="Enter username.")
        parser.add_argument(
            "password",
            required=True,
            help="Enter password.")
        args = parser.parse_args()
        firstname, lastname,  username, password = args["firstname"], args[
            "lastname"], args["username"], args["password"]
        data = {
            "firstname": firstname,
            "lastname": lastname,
            "username": username,
            "password": password
        }
        # Add to database
        add_user(data)

        response = {
            "status": "ok",
            "message": "User has been Registered"
        }
        return (response), 201


class User_Login(Resource):
    """
        Log in an existing user
    """

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(
            "username",
            required=True,
            help="Please enter a username.")
        parser.add_argument(
            "password",
            required=True,
            help="Please enter a password.")

        args = parser.parse_args()

        username, password = args["username"], args["password"]

        if login(username, password) == True:
            access_token = create_access_token(identity=username)
            return access_token, 200
        else:
            return {
                "status": "Failed",
                "message": "Invalid credentials"
            }, 400

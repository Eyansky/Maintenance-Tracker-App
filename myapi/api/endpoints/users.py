from flask_restful import Resource
from flask_restful import reqparse
from myapi.api.resources.serializers import user_serializer

class UserRegister(Resource):
    """
    Register a new user.
    """

    def post(self):
        """ Add a user """
        parser = reqparse.RequestParser()
        parser.add_argument( "firstname",
            required=True,
            help="Enter first name")
        parser.add_argument( "lastname",
            required=True,
            help="Enter last name")
        parser.add_argument( "username",
            required=True,
            help="Enter username.")
        parser.add_argument(
            "password",
            required=True,
            help="Enter password.")
        args = parser.parse_args()
        firstname, lastname,  username, password = args["firstname"],args["lastname"],args["username"], args["password"]
        data = {
            "firstname":firstname,
            "lastname":lastname,
            "username":username,
            "password":password
        }
        return (data),201


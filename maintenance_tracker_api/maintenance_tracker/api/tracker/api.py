from flask import Flask, request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

class User(object):
    def __init__(self):
        self.total = 0
        self.user = {}

    def add_user(self, firstname, lastname, username, password):
        self.total += 1
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password = password
        self.user["firstname"] = self.firstname
        self.user["lastname"] = self.lastname
        self.user["username"] = self.username
        self.user["password"] = self.password
       
        
    def userDetails(self):
        return self.user.values()

class Registration(Resource):
    """
    Register a new user.
    """

    def post(self):
        """ Add a user """
        parser = reqparse.RequestParser()
        parser.add_argument( "firstname",required=True, help="Enter first name.")
        parser.add_argument( "lastname",required=True, help="Enter last name")
        parser.add_argument( "username",required=True, help="Enter username")
        parser.add_argument( "password", required=True, help="Enter Password")

        args = parser.parse_args()

        firstname, lastname, username, password = args["firstname"], args["lastname"], args["username"], args["password"]
        user =User()
        User.add_user(firstname=firstname,lastname=lastname,username=username, password=password)
        return {"user": firstname}


api.add_resource(Registration, "/api/v1/register")


if __name__ == "__main__":
    app.run(debug=True)

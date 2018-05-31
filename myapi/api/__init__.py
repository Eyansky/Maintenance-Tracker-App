from flask import Flask
from flask_restful import Api
from myapi.api.endpoints.users import UserRegister

app = Flask(__name__)
api = Api(app)

api.add_resource(UserRegister, '/api/v1/users/register')
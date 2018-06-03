from flask import Flask
from flask_restful import Api
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
from myapi.api.endpoints.users import User_Register, User_Login
from myapi.api.endpoints.requests import Create_Request

app = Flask(__name__)
api = Api(app)

app.config['JWT_SECRET_KEY'] = 'ianeyansky'
jwt = JWTManager(app)

api.add_resource(User_Register, '/api/v1/users/register')
api.add_resource(User_Login, '/api/v1/users/login')
api.add_resource(Create_Request, '/api/v1/users/requests')

from flask import Flask
from flask_restful import Api
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity, get_jwt_claims)

from myapi.api.endpoints.users import UserRegister, UserLogin
from myapi.api.endpoints.requests import Request
from myapi.api.endpoints.admin import admin, AdminApprove, AdminDisaprove


app = Flask(__name__)
api = Api(app)

app.config['JWT_SECRET_KEY'] = 'ianeyansky'
jwt = JWTManager(app)

# This is what we want stored in our tokens
"""
class UserObject:
    def __init__(self, username, roles):
        self.username = username
        self.roles = roles

# lets us define what custom claims should be added to the access token.


@jwt.user_claims_loader
def add_claims_to_access_token(user):
    return {'roles': roles}

# lets us define what the identity of the access token should be.


@jwt.user_identity_loader
def user_identity_lookup(user):
    return username
"""

api.add_resource(UserRegister, '/api/v2/auth/signup')
api.add_resource(UserLogin, '/api/v2/auth/login')
api.add_resource(Request, '/api/v2/users/requests')
api.add_resource(Request, '/api/v2/users/requests/<int:id>')
# Admin endpoints
api.add_resource(admin, '/api/v2/requests')
api.add_resource(AdminApprove, '/api/v2/requests/<int:id>/approve')
api.add_resource(AdminDisaprove, '/api/v2/requests/<int:id>/disapprove')


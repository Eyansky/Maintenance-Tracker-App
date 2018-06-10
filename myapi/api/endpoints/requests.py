from flask_restful import Resource
from flask import request
import requests
from flask_jwt_extended import JWTManager, jwt_required, \
    create_access_token, get_jwt_identity, get_jwt_claims

from myapi.api.database.models import add_request, allrequests


class Request(Resource):

    # all requests  
    @jwt_required
    def get(self):
        username = get_jwt_identity()
        result = allrequests(username)
        return (result), 200


    # single request
    @jwt_required
    def get(self, id):
        username = get_jwt_identity()
        request = get_request_id(username, id)
        if not request:
            return {
                "status": "err",
                "message": "Reqeust not found"
            }, 404
        return (request), 200 
  
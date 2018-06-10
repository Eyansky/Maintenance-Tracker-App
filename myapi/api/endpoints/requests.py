from flask_restful import Resource
from flask import request
import requests
from flask_jwt_extended import JWTManager, jwt_required, \
    create_access_token, get_jwt_identity, get_jwt_claims

from myapi.api.database.models import add_request, allrequests


class Request(Resource):
         
    def is_valid(item):
        """ 
        checking for valid credentials
        """
        errors = {}
        if not item.get("title"):
            errors["title"] = "title Details are required."

        if not item.get("request"):
            errors["request"] = "Reuest Details are required."

        return len(errors) == 0, errors

    @jwt_required
    def post(self):
        if request.is_json:
            valid, errors = self.is_valid(request.json)
            if not valid:
                return {"status": "error", "data": errors}, 400
            result = request.json
            
            title=result['title']
            request=result['request']
            username=get_jwt_identity()
            status = "Pending"

            request = {
                "username": username,
                "title": title,
                "request": request,
                "status":status}
            

            return {"status": "success", "data": "request has been created"}, 201
        else:
            return {"message": "Request should be in JSON", "status": "error"}, 400

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
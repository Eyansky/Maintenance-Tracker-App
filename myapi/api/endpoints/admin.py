from flask_restful import Resource
from flask import request
import requests
from flask_jwt_extended import JWTManager, jwt_required, \
    create_access_token, get_jwt_identity, get_jwt_claims

from myapi.api.database.models import add_request, allrequests, adminrequests, adminApproveDisapprove


class admin(Resource):

    # all requests  for admin
    @jwt_required
    def get(self):
        result = adminrequests()
        return (result), 200
    
class AdminApprove(Resource):

    def is_valid(item):
        """ 
        checking for valid credentials
        """
        errors = {}
        if not item.get("id"):
            errors["id"] = "Id is required."

        return len(errors) == 0, errors
    
    @jwt_required
    def put(self):
        if request.is_json:
            valid, errors = self.is_valid(request.json)
            if not valid:
                return {"status": "error", "data": errors}, 400
            result = request.json
            
            id=result['id']
            status="Approved"

            request = {
                "id": id,
                "status": status}
            # Approve to db
            state = adminApproveDisapprove(request)

            return {"status": "success", "details": state}, 201
        else:
            return {"message": "Request should be in JSON", "status": "error"}, 400

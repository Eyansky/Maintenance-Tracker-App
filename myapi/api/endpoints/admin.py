from flask_restful import Resource
from flask import request
from flask_jwt_extended import JWTManager, jwt_required, \
    create_access_token, get_jwt_identity, get_jwt_claims

from myapi.api.database.models import add_request, allrequests, adminrequests, adminApproveDisapprove, roles, AdminResolve


class admin(Resource):

    # all requests  for admin
    @jwt_required
    def get(self):
        username = get_jwt_identity()
        role = roles(username)
        if role == Admin:
            result = adminrequests()
            return (result), 200
        else:
            return {"status": "Only Admins allowed"}


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
    def put(self, id):
        username = get_jwt_identity()
        role = roles(username)
        if role == Admin:
            if self.request.is_json:
                valid, errors = self.is_valid(self.request.json)
                if not valid:
                    return {"status": "error", "data": errors}, 400
                result = self.request.json

                id = result['id']
                status = "Approved"

                request = {
                    "id": id,
                    "status": status}
                # Approve to db
                state = adminApproveDisapprove(request)

                return {"status": "success", "details": state}, 201
            else:
                return {"message": "Request should be in JSON", "status": "error"}, 400
        else:
            return {"status": "Only Admins allowed"}


class AdminDisaprove(Resource):

    def is_valid(item):
        """ 
        checking for valid credentials
        """
        errors = {}
        if not item.get("id"):
            errors["id"] = "Id is required."

        return len(errors) == 0, errors

    @jwt_required
    def put(self, id):
        username = get_jwt_identity()
        role = roles(username)
        if role == Admin:
            if self.request.is_json:
                valid, errors = self.is_valid(self.request.json)
                if not valid:
                    return {"status": "error", "data": errors}, 400
                result = self.request.json

                id = result['id']
                status = "Disapproved"

                request = {
                    "id": id,
                    "status": status}
                # Approve to db
                state = adminApproveDisapprove(request)

                return {"status": "success", "details": state}, 201
            else:
                return {"message": "Request should be in JSON", "status": "error"}, 400
        else:
            return {"status": "Only Admins allowed"}


class AdminResolve(Resource):

    def is_valid(item):
        """ 
        checking for valid credentials
        """
        errors = {}
        if not item.get("id"):
            errors["id"] = "Id is required."

        if not item.get("resolve"):
            errors["resolve"] = "Resolution is required."

        return len(errors) == 0, errors

    @jwt_required
    def put(self, item):
        username = get_jwt_identity()
        role = roles(username)
        if role == Admin:
            if self.request.is_json:
                valid, errors = self.is_valid(self.request.json)
                if not valid:
                    return {"status": "error", "data": errors}, 400
                result = self.request.json

                id = result['id']
                resolve = result['resolve']
                status = "Resolved"

                request = {
                    "id": id,
                    "resolve": resolve,
                    "status": status}
                # Approve to db
                state = AdminResolve(request)

                return {"status": "success", "details": state}, 201
            else:
                return {"message": "Request should be in JSON", "status": "error"}, 400
        else:
            return {"status": "Only Admins allowed"}

from flask_restful import Resource
from flask_restful import reqparse
from myapi.api.resources.serializers import request_serializer
from flask_jwt_extended import (
    jwt_required, get_jwt_identity
)

from myapi.api.database.db import (
    add_request, view_user_requests)


class Create_Request(Resource):
    """
    Create a request
    """
    @jwt_required
    def post(self):
        """ Add a request """
        parser = reqparse.RequestParser()
        parser.add_argument("title",
                            required=True,
                            help="Enter Title")
        parser.add_argument(
            "request",
            required=True,
            help="Enter Request details...")

        args = parser.parse_args()

        title, request = args["title"], args["request"]
        username = get_jwt_identity()
        data = {
            "username": username,
            "title": title,
            "request": request
        }
        # Add to database
        add_request(data)

        response = {
            "status": "ok",
            "message": "Request has been added"
        }
        return (response), 201

    @jwt_required
    def get(self):
        username = get_jwt_identity()
        result = view_user_requests(username)
        return (result), 200

from flask_restful import Resource
from flask_restful import reqparse
from myapi.api.resources.serializers import request_serializer
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)

from myapi.api.resources.models import add_request, view_requests


class Create_Request(Resource):
    """
    Create a request
    """
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
        data = {
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

    def get(self):
        return (view_requests()), 200

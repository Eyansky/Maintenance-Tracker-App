from flask_restful import Resource
from flask_restful import reqparse
from flask_jwt_extended import (
    jwt_required, get_jwt_identity
)


from myapi.api.resources.models import (
    get_request_id, edit_request)


class SingleRequest(Resource):
    """
    Single Request
    """

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

    @jwt_required
    def put(self, id):
        username = get_jwt_identity()
        request = get_request_id(username, id)
        if not request:
            return {
                "status": "err",
                "message": "Reqeust not found"
            }, 404

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
        # Add to database
        edit_request(username, id, title, request)

        response = {
            "status": "ok",
            "message": "Request has been edited"
        }
        return (response), 201

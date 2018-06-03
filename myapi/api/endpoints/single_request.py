from flask_restful import Resource
from flask_restful import reqparse
from flask_jwt_extended import (
    jwt_required, get_jwt_identity
)

from myapi.api.resources.models import (
    get_request_id)


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

from flask_restful import Resource
from flask import request
from flask_jwt_extended import JWTManager, jwt_required, \
    create_access_token, get_jwt_identity, get_jwt_claims

from myapi.api.database.models import add_request, allrequests, get_request_id, modify, status


class Request(Resource):

    """
       Create Request
      ---
      tags:
           - The requests API
      parameters:

        - in: formData
          name: title
          type: string
          required: true

        - in: formData
          name: Request
          type: string
          required: true
      responses:
        201:
          description: request has been created.
    """



    def is_valid(self, item):
        """ 
        checking for valid credentials
        """
        errors = {}
        if not item.get("title"):
            errors["title"] = "title Details are required."

        if not item.get("request"):
            errors["request"] = "Request Details are required."

        return len(errors) == 0, errors

    @jwt_required
    def post(self):
        from flask import request
        # import pdb; pdb.set_trace()
        # print('=========>>>>>>>>>', self.request)
        if self.request.is_json == True:
            valid, errors = self.is_valid(self.request.json)
            if not valid:
                return {"status": "error", "data": errors}, 400
            result = self.request.json

            title = result['title']
            request = result['request']
            username = get_jwt_identity()
            status = "Pending"

            request = {
                "username": username,
                "title": title,
                "request": request,
                "status": status}
            # adding to db    
            add_request(request)

            return {"status": "success", "data": "request has been created"}, 201
        else:
            return {"message": "Request should be in JSON",
                    "status": "error"}, 400


    # all requests
    @jwt_required
    def get(self):
        username = get_jwt_identity()
        result = allrequests(username)
        return (result), 200



class SingleRequests(Resource):
    """
       Create single Request
      ---
      tags:
           - The requests API
      parameters:
       
        - in: formData
          name: id
          type: int
          required: true

      responses:
        201:
          description: request has been created.
       """
    # single request
    @jwt_required
    def get(self, id):
        username = get_jwt_identity()
        request = get_request_id(username, id)
        if not request:
            return {
                "status": "err",
                "message": "Request not found"
            }, 404
        return (request), 200

class ModifyRequest(Resource):
    from flask import request

    def is_valid(self, item):
        """ 
        checking for valid credentials
        """
        errors = {}
        
        if not item.get("title"):
            errors["title"] = "Title is required."
        
        if not item.get("request"):
            errors["request"] = "Request is required."

        return len(errors) == 0, errors

    # @jwt_required
    def put(self, id):
        if self.request.is_json == True:
            valid, errors = self.is_valid(self.request.json)
            if not valid:
                return {"status": "error", "data": errors}, 400
            result = self.request.json

            data = {
                "id": id,
                "title": result['title'],
                "request": result['request'] }
            # Approve to db
            
            # import pdb; pdb.set_trace() 
            state = modify(data)
            import pdb; pdb.set_trace() 
            return {"status": "success", "details": state}, 201
        
        else:
            return {"message": "Request should be in JSON",
                    "status": "error"}, 400
        


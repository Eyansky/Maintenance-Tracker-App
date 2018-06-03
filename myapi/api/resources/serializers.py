from flask_restful import fields

"""
 use a schema
"""

user_serializer = {
    "firstname":fields.String,
    "lastname":fields.String,
    "username": fields.String,
    "password":fields.String
}

request_serializer = {
    "Title":fields.String,
    "Details":fields.String
}
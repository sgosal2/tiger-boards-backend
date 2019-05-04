from flask import request, jsonify, make_response
from flask_jwt_extended import (
    create_access_token, create_refresh_token, jwt_refresh_token_required,
    get_jwt_identity
)
from flask_restplus import Namespace, Resource
from utilities import database_utilities

api = Namespace("login", description="Endpoint used to obtain JWT")


@api.route('/')
class Login(Resource):
    def post(self):
        """ Returns JWT upon login verification """
        json_data = request.get_json()
        if 'email' not in json_data or not json_data['email']:
            return make_response(jsonify(msg="Missing email"), 401)

        data = database_utilities.execute_query(
            "SELECT * FROM admins WHERE email = %s", (json_data['email'], ))
        return jsonify({"is_admin": len(data) > 0})


@api.route('/refresh')
class Refresh(Resource):
    def post(self):
        current_user = get_jwt_identity()
        access_token = create_access_token(identity=current_user)

        resp = jsonify({"refresh_token": access_token})
        return resp

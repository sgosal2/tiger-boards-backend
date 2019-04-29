from flask import request, jsonify
from flask_jwt_extended import create_access_token
from flask_restplus import Namespace, Resource
from utilities import database_utilities

api = Namespace("login", description="Endpoint used to obtain JWT")


@api.route('/')
class Login(Resource):
    def post(self):
        """ Returns JWT upon login verification """
        json_data = request.get_json()
        if not json_data['email']:
            return jsonify({"msg": "Missing email"}), 400

        data = database_utilities.execute_query(
            f"""select * from admins where email = '{json_data['email']}'""")
        if data:
            access_token = create_access_token(identity=data[0]['email'])
            return jsonify(access_token=access_token)
        else:
            return jsonify({"msg": "User is not an admin"})

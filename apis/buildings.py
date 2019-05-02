from flask import request, jsonify
from flask_restplus import Namespace, Resource, fields

from utilities.database_utilities import execute_query

api = Namespace("buildings", description="Information relating to buildings")


@api.route('/')
class Buildings(Resource):
    def get(self):
        """Fetch data for all buidlings."""
        return execute_query("SELECT * FROM building")

    def post(self):
        """Insert new building."""
        query = "INSERT INTO building VALUES (%s, %s)"
        json_data = request.get_json()
        parameters = (json_data['building_id'], json_data['building_name'])
        execute_query(query, parameters)
        return jsonify(msg="Insert successful.")


@api.route('/<string:building_id>')
class Building(Resource):
    def patch(self, building_id):
        """Edit a building info."""
        query = """
            UPDATE building
            SET building_name = %s, building_id = %s 
            WHERE building_id = %s
            """
        json_data = request.get_json()
        parameters = (json_data['new_name'], json_data['new_id'], building_id)
        execute_query(query, parameters)
        return jsonify(msg="Edit successful.")

    def delete(self, building_id):
        """Delete a building"""
        query = "DELETE FROM building WHERE building_id = %s"
        parameters = (building_id,)
        execute_query(query, parameters)
        return jsonify(msg="Delete successful.")

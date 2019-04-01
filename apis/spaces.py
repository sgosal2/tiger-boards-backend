from flask import request
from flask_restplus import Namespace, Resource, fields
from utilities import database_utilities

api = Namespace("spaces", description="Information relating to spaces")


@api.route('/')
class Spaces(Resource):
    def get(self):
        """ Fetch data for all spaces """
        return database_utilities.execute_query("select * from spaces")

    def post(self):
        """ Insert data for new space """
        query = f"""insert into spaces values (%s, %s, %s, %s, %s);"""
        parameters = (request.form['space_id'], request.form['building_id'],
                      request.form['name'], request.form['capacity'],
                      request.form['features'])
        database_utilities.execute_query(query, parameters)


@api.route('/<string:space_id>')
class Space(Resource):
    def get(self, space_id):
        """ Fetch data for space based on space_id """
        return database_utilities.execute_query(
            f"""select * from spaces where space_id = '{space_id}'""")

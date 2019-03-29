from flask_restplus import Namespace, Resource, fields
from utilities import database_utilities

api = Namespace("spaces", description="Information relating to spaces")


@api.route('/')
class Spaces(Resource):
    def get(self):
        """ Fetch data for all spaces """
        return database_utilities.execute_query("select * from spaces")


@api.route('/<string:space_id>')
class Space(Resource):
    def get(self, space_id):
        """ Fetch data for space based on space_id """
        return database_utilities.execute_query(
            f"""select * from spaces where space_id = '{space_id}'""")

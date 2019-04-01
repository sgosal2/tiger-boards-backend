from flask_restplus import Namespace, Resource, fields
from utilities import database_utilities

api = Namespace("spaces", description="Information relating to spaces")


@api.route('/')
class Spaces(Resource):
    def get(self):
        return database_utilities.execute_query("select * from spaces")

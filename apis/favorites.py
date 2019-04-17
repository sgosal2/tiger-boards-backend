from flask import request
from flask_restplus import Namespace, Resource, fields
from utilities import database_utilities

api = Namespace("favorites", description="Information relating to favorites")

@api.route('/')
class Favorites(Resource):
    def get(self):
        """ Fetch data for all favorites """
        return database_utilities.execute_query("select * from favorites")

    def post(self):
        """ Insert data for new favorites """
        query = f"""insert into favorites values (%s, %s);"""
        parameters = (request.form['user_id'], request.form['favorite_spaces'])
        database_utilities.execute_query(query, parameters)

@api.route('/<string:user_id>')
class Favorite(Resource):
    def get(self, user_id):
        """ Fetch data for favorite with the corresponding user_id """
        return database_utilities.execute_query(
            f"""select * from favorites where user_id = '{user_id}'""")

    def delete(self, user_id):
        """ Deletes favorite with the corresponding user_id """
        return database_utilities.execute_query(
            f"""delete from favorites where user_id = %s""", (user_id, ))

    def patch(self, user_id):
        """ Replaces information of corresponding user_id with request body """
        query = f"""update favorites set user_id = %s, favorite_spaces = %s """
        query += f"""where user_id = '{user_id}'"""
        parameters = (request.form['user_id'], request.form['favorite_spaces'])
        database_utilities.execute_query(query, parameters)
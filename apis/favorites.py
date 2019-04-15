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
        parameters = (request.form['user_email'], request.form['favorite_spaces'])
        database_utilities.execute_query(query, parameters)

@api.route('/<string:user_email>')
class Favorite(Resource):
    def get(self, user_email):
        """ Fetch data for favorite with the corresponding user_email """
        return database_utilities.execute_query(
            f"""select * from favorites where user_email = '{user_email}'""")

    def delete(self, user_email):
        """ Deletes favorite with the corresponding user_email """
        return database_utilities.execute_query(
            f"""delete from favorites where user_email = %s""", (user_email, ))

    def patch(self, user_email):
        """ Replaces information of corresponding user_email with request body """
        query = f"""update favorites set user_email = %s, favorite_spaces = %s """
        query += f"""where user_email = '{user_email}'"""
        parameters = (request.form['user_email'], request.form['favorite_spaces'])
        database_utilities.execute_query(query, parameters)
from flask import request
from flask_restplus import Namespace, Resource, fields
from utilities import database_utilities

api = Namespace("user_settings",
                description="Information relating to user settings")


@api.route('/')
class User_Settings(Resource):
    def get(self):
        """ Fetch data for all user_settings """
        return database_utilities.execute_query("select * from user_settings")

    def post(self):
        """ Insert data for new user_settings """
        query = f"""insert into user_settings values (%s, %s, %s);"""
        json_data = request.get_json()
        parameters = (json_data['user_id'], json_data['daily_email'],
                      json_data['weekly_email'])
        database_utilities.execute_query(query, parameters)


@api.route('/<string:user_id>')
class User_Setting(Resource):
    def get(self, user_id):
        """ Fetch data for user_settings with corresponding user_id """
        return database_utilities.execute_query(f"""select * from user_settings where user_id = '{user_id}'""")

    def delete(self, user_id):
        """ Deletes user_settings with the corresponding user_id """
        return database_utilities.execute_query(f"""delete from user_settings where user_id = '{user_id}'""")

    def patch(self, user_id):
        """ Replaces information of corresponding user_id with request body """
        query = f"""update user_settings set user_id = %s, daily_email = %s, weekly_email = %s """
        query += f"""where user_id = '{user_id}'"""
        json_data = request.get_json()
        parameters = (json_data['user_id'], json_data['daily_email'],
                      json_data['weekly_email'])
        database_utilities.execute_query(query, parameters)

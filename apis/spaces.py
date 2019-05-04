from flask import request, jsonify
from flask_jwt_extended import jwt_required
from flask_restplus import Namespace, Resource, fields, reqparse

from datetime import datetime, time
from time import mktime

from utilities import (
    convert_datetimes_in_query_results,
    get_day_of_the_week_from_datetime,
    get_semester_from_datetime,
    parse_datetime
)
from utilities.database_utilities import execute_query

api = Namespace("spaces", description="Information relating to spaces")


@api.route('/')
class Spaces(Resource):
    def get(self):
        """ Fetch data for all spaces """

        # Parse request for parameters
        parser = reqparse.RequestParser()
        parser.add_argument('building_id')
        parser.add_argument('datetime')
        args = parser.parse_args()

        # Build query strings
        where_query = "WHERE building_id = %s" if args['building_id'] else ''
        query = f"SELECT * FROM spaces {where_query}"
        parameters = (args['building_id'],)

        spaces_query_results = execute_query(query, parameters)

        # If provided a datetime, get availability data
        if args['datetime'] and args['building_id']:
            # Get events of queried spaces
            space_ids = [row["space_id"] for row in spaces_query_results]
            events_query_results = execute_query(
                "SELECT * FROM class WHERE space_id IN %s", (tuple(space_ids),))

            datetime_obj = parse_datetime(args["datetime"])
            day_of_the_week = get_day_of_the_week_from_datetime(datetime_obj)
            time_obj = datetime_obj.time()
            current_semester = get_semester_from_datetime(datetime_obj)

            for space in spaces_query_results:
                space["is_available"] = "Available"
                for event in events_query_results:
                    # Check matching space_id and semester_id
                    if (space["space_id"] == event["space_id"]
                            and event["semester_id"] == current_semester):
                        # Check day
                        day_check = day_of_the_week in list(event["days"])

                        # Check time
                        time_check = (event["start_time"] < time_obj
                                      and time_obj < event["end_time"])

                        if day_check and time_check:
                            space["is_available"] = event["class_title"]
                            break

        return spaces_query_results

    @jwt_required
    def post(self):
        """ Insert data for new space """
        query = f"""insert into spaces values (%s, %s, %s, %s, %s);"""
        json_data = request.get_json()
        parameters = (json_data['space_id'], json_data['building_id'],
                      json_data['name'], json_data['capacity'],
                      json_data['features'])
        execute_query(query, parameters)
        return jsonify(msg="Insert successful.")


@api.route('/<string:space_id>')
class Space(Resource):
    def get(self, space_id):
        """ Fetch data for space with the corresponding space_id """
        return database_utilities.execute_query(
            f"""select * from spaces where space_id = %s""", (space_id, ))

    @jwt_required
    def delete(self, space_id):
        """ Deletes space with the corresponding space_id """
        execute_query(
            "DELETE FROM spaces WHERE space_id = %s", (space_id, ))
        return jsonify(msg="Delete successful.")

    @jwt_required
    def patch(self, space_id):
        """Updates a space record."""

        json_data = request.get_json()
        parameters = []
        set_query = []
        space_attributes = ["space_id", "building_id",
                            "name", "capacity", "features"]

        for attr in space_attributes:
            if attr in json_data:
                set_query.append(f"{attr} = %s")
                parameters.append(json_data[attr])

        set_query = ", ".join(set_query)
        parameters.append(space_id)
        parameters = tuple(parameters)
        query = f"UPDATE spaces SET {set_query} WHERE space_id = %s"
        print(query)
        print(parameters)
        execute_query(query, parameters)
        return jsonify(msg="Edit successful.")

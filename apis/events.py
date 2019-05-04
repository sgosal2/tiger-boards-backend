from flask import request, jsonify
from flask_restplus import Namespace, Resource, fields, reqparse

from utilities import convert_datetimes_in_query_results
from utilities.database_utilities import execute_query

api = Namespace("events", description="Information relating to events.")


@api.route('/')
class Events(Resource):
    def get(self):
        """Fetch data for all events."""

        # Parse request for parameters
        parser = reqparse.RequestParser()
        parser.add_argument('space_id')
        args = parser.parse_args()

        # Build query strings
        where_query = "WHERE space_id = %s" if args['space_id'] else ''
        query = f"SELECT * FROM class {where_query}"
        parameters = (args['space_id'],)

        results = execute_query(query, parameters)

        convert_datetimes_in_query_results(results)

        print(results)
        return results

    def post(self):
        """Insert new event."""
        query = """
            INSERT INTO class
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
        json_data = request.get_json()
        parameters = (
            json_data['class_title'],
            json_data['subject'],
            json_data['course_num'],
            json_data['start_time'],
            json_data['end_time'],
            json_data['days'],
            json_data['space_id'],
            json_data['instructor_first'],
            json_data['instructor_last'],
            json_data['semester_id'],
            json_data['crn'],
        )
        execute_query(query, parameters)
        return jsonify(msg="Insert successful.")


@api.route('/<string:event_id>')
class Event(Resource):
    def patch(self, event_id):
        """Edit an event info."""

        json_data = request.get_json()
        parameters = []
        set_query = []
        event_attributes = ["class_title", "subject",
                            "course_num", "start_time", "end_time", "days", "space_id", "instructor_first", "instructor_last", "semester_id", "crn"]

        for attr in event_attributes:
            if attr in json_data:
                set_query.append(f"{attr} = %s")
                parameters.append(json_data[attr])

        set_query = ", ".join(set_query)
        parameters.append(f"{json_data['crn']}{json_data['semester_id']}")
        parameters = tuple(parameters)
        query = f"UPDATE class SET {set_query} WHERE CONCAT(crn, semester_id) = %s"
        print(query)
        print(parameters)
        execute_query(query, parameters)
        return jsonify(msg="Edit successful.")

    def delete(self, event_id):
        """Delete an event"""
        query = "DELETE FROM class WHERE CONCAT(crn, semester_id) = %s"
        parameters = (event_id,)
        execute_query(query, parameters)
        return jsonify(msg="Delete successful.")

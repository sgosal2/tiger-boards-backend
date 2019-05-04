from datetime import datetime

from utilities.database_utilities import execute_query


def get_day_of_the_week_from_datetime(datetime_obj):
    """Convert datetime weekday number to single letter coding."""

    return list("MTWRFSU")[datetime_obj.weekday()]


def get_semester_from_datetime(datetime_obj):
    """Find semester record that intersects with given datetime object."""

    return execute_query(
        """
        SELECT * 
        FROM semester 
        WHERE start_date <= %s AND end_date > %s""",
        (datetime_obj, datetime_obj))[0]["semester_id"]


def parse_datetime(datetime_str):
    """Parse datetime string from datepicker in front-end."""

    return datetime.strptime(datetime_str, '%Y-%m-%dT%H:%M')

import datetime

from .time import (
    get_day_of_the_week_from_datetime,
    get_semester_from_datetime,
    parse_datetime
)


def convert_datetimes_in_query_results(query_results):
    if not query_results:
        return

    for row in query_results:
        for col in row:
            if type(row[col]) == datetime.time:
                row[col] = str(row[col])

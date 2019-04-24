from datetime import time


def convert_datetimes_in_query_results(query_results):
    for row in query_results:
        for col in row:
            if type(row[col]) == time:
                row[col] = str(row[col])

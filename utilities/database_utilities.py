import config
import os
import psycopg2


def execute_query(query):
    conn = psycopg2.connect(config.DATABASE["url"], sslmode='require')
    cur = conn.cursor()
    cur.execute(query)
    try:
        data = cur.fetchall()
    # If there is no data being fetched, data variable is set to null
    except psycopg2.ProgrammingError:
        data = None
    finally:
        conn.commit()

        # Format data to include column names
        if data:
            results = []
            for row in data:
                row_to_append = {}
                col_index = 0
                for col in cur.description:
                    row_to_append[col[0]] = row[col_index]
                    col_index += 1
                results.append(row_to_append)

            cur.close()
            conn.close()
            return results

        cur.close()
        conn.close()

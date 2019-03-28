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
        cur.close()
        conn.close()
        if data:
            return data

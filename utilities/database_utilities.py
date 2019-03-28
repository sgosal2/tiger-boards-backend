import config
import os
import psycopg2


def execute_query(query):
    conn = psycopg2.connect(config.DATABASE["url"], sslmode='require')
    cur = conn.cursor()
    cur.execute(query)
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data

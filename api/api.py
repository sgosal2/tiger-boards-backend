from flask import Flask
from flask_restplus import Resource, Api

import os
import psycopg2

DATABASE_URL = 'postgres://hcjjfhapqzkpxr:de1fed54423d85bd173367ba3700b89679226c1e9ad138f4a059c707fbd5fee7@ec2-54-225-95-183.compute-1.amazonaws.com:5432/dfcmct49s0bl0t'

app = Flask(__name__)
api = Api(app)

@api.route('/spaces')
class HelloWorld(Resource):
    def get(self):
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        cur = conn.cursor()
        cur.execute("SELECT * FROM spaces;")
        data = cur.fetchall()
        cur.close()
        conn.close()
        return data

if __name__ == '__main__':
    app.run(debug=True)
from apis import api
from flask import Flask
from flask_restplus import Resource, Api
import os
import psycopg2


app = Flask(__name__)
api.init_app(app)


@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Methods'] = '*'
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

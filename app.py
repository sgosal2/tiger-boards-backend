from apis import api
from flask import Flask
from flask_restplus import Resource, Api
import os
import psycopg2


app = Flask(__name__)
api.init_app(app)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

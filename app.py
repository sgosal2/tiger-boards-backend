from apis import api
from flask import Flask
from flask_restplus import Resource, Api
from flask_jwt_extended import JWTManager
import os
import psycopg2

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'v-secret'
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_COOKIE_SECURE'] = False
app.config['JWT_ACCESS_COOKIE_PATH'] = '/'
app.config['JWT_REFRESH_COOKIE_PATH'] = '/login'
app.config['JWT_COOKIE_CSRF_PROTECT'] = True
jwt = JWTManager(app)
api.init_app(app)


@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)

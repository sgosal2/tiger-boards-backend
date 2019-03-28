from flask_restplus import Api
from .spaces import api as spaces_api

api = Api(
    title="Tiger Boards API",
    version="0.1",
    description="API used to communicate with Postgres SQL database for Tiger Boards"
)

api.add_namespace(spaces_api)

from flask_restplus import Api
from .admins import api as admins_api
from .buildings import api as buildings_api
from .events import api as events_api
from .login import api as login_api
from .spaces import api as spaces_api
from .users import api as users_api


api = Api(
    title="Tiger Boards API",
    version="0.1",
    description="API used to communicate with Postgres SQL database for Tiger Boards"
)

api.add_namespace(admins_api)
api.add_namespace(buildings_api)
api.add_namespace(events_api)
api.add_namespace(login_api)
api.add_namespace(spaces_api)
api.add_namespace(users_api)

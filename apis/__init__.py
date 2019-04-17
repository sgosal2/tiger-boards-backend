from flask_restplus import Api
from .admins import api as admins_api
from .favorites import api as favorites_api
from .spaces import api as spaces_api
<<<<<<< HEAD
from .user_settings import api as user_settings_api
=======
from .users import api as users_api
>>>>>>> 86e847ae221a6f17c9aead7c4c5869505995498d


api = Api(
    title="Tiger Boards API",
    version="0.1",
    description="API used to communicate with Postgres SQL database for Tiger Boards"
)

api.add_namespace(spaces_api)
api.add_namespace(favorites_api)
api.add_namespace(admins_api)
<<<<<<< HEAD
api.add_namespace(user_settings_api)
=======
api.add_namespace(users_api)
>>>>>>> 86e847ae221a6f17c9aead7c4c5869505995498d

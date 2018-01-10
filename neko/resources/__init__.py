from flask_restful import Api
from .post import PostResource

api = Api()

api.add_resource(PostResource, '/posts', '/posts/', '/posts/<string:id>')

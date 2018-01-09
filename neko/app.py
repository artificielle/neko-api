from flask import Flask
from flask_restful import Api
from .resources.post import PostResource

app = Flask(__name__)

api = Api(app)

api.add_resource(PostResource, '/posts', '/posts/', '/posts/<string:id>')

def main():
  app.run(debug=True)

from flask import Flask
from .models import db
from .resources import api

def create_app():
  # pylint: disable = redefined-outer-name
  app = Flask(__name__)

  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  app.config['SQLALCHEMY_ECHO'] = app.debug

  api.init_app(app)
  db.init_app(app)

  return app

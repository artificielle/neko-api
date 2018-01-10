from flask import Flask
from .models import db
from .resources import api

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api.init_app(app)

db.init_app(app)

def main():
  from .models.db_init import db_init
  db_init(app)
  app.run(debug=True)

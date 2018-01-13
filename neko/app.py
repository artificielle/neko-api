from . import create_app

app = create_app()

if app.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:///:memory:':
  from .models.db_init import db_init
  db_init(app)

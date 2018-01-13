from datetime import datetime
from flask import Flask
from . import db
from .post import Post

def db_init(app: Flask):
  with app.app_context():
    if app.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:///:memory:':
      db.create_all()
      if app.debug and not app.testing:
        # pylint: disable = no-member
        db.session.add_all(map(mock_post, range(1, 51)))
        db.session.commit()

def mock_post(i):
  return Post(
    time=datetime(year=2222, month=2, day=2, second=i),
    link=f'https://example.org/posts/{i}',
    site=f'Site {i}',
    title=f'Title {i}',
    author=f'Author {i}',
    summary=f'Summary {i}',
  )

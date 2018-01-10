from datetime import datetime
from . import db
from .post import Post

def db_init(app):
  with app.app_context():
    db.create_all()
    db.session.add(Post(
      time=datetime.now(),
      link='https://example.org/posts/1',
      site='YGGDRASIL',
      title='Albedo',
      author='Tabula Smaragdina',
      summary='Balabala..',
    ))
    db.session.add(Post(
      time=datetime.now(),
      link='https://example.org/posts/2',
      site='YGGDRASIL',
      title='Shalltear Bloodfallen',
      author='Peroroncino',
      summary='Balabala..',
    ))
    db.session.commit()

from datetime import datetime
from . import db
from .post import Post

def db_init(app):
  with app.app_context():
    # pylint: disable = no-member
    db.create_all()
    for i in range(1, 51):
      db.session.add(Post(
        time=datetime(year=2222, month=2, day=2, second=i),
        link=f'https://example.org/posts/{i}',
        site=f'Site {i}',
        title=f'Title {i}',
        author=f'Author {i}',
        summary=f'Summary {i}',
      ))
    db.session.commit()

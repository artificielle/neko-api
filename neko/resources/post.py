from typing import List, NamedTuple
from datetime import datetime
from flask_restful import Resource
from ..common.util import marshal, namedtuple_fields

class Post(NamedTuple):
  id: str
  link: str
  time: datetime
  site: str
  title: str
  author: str
  summary: str
  tags: List[str] = []

post_fields = namedtuple_fields(Post)

class PostResource(Resource):

  def get(self, id=None):
    post = Post(
      id=id or '',
      link='https://example.org/posts/1',
      time=datetime.now(),
      site='YGGDRASIL',
      title='Shalltear',
      author='Peroroncino',
      summary='Balabala..',
      tags=['Ainz Ooal Gown', 'Valkyrie'],
    )
    post_dict = marshal(post, post_fields)
    if id:
      return post_dict
    else:
      return {'data': [post_dict], 'page_size': 20}

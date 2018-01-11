from flask_restful import Resource, marshal, reqparse
from ..common.util import hashid_decode
from ..models.post import Post

class PostResource(Resource):

  def get(self, id=None):
    return self.get_one(id) if id else self.get_all()

  def get_all(self):
    parser = reqparse.RequestParser()
    parser.add_argument('cursor')
    args = parser.parse_args()
    if args['cursor']:
      return None, 501
    else:
      pagination = Post.query.paginate(max_per_page=20)
      return {
        'data': marshal(pagination.items, Post.fields),
        'page': pagination.page,
        'per_page': pagination.per_page,
      }

  def get_one(self, id):
    post = Post.query.filter_by(link=hashid_decode(id)).first_or_404()
    return marshal(post, Post.fields)

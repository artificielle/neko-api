from flask_restful import Resource, marshal_with, reqparse
from ..common.util import pagination_fields, id_decode
from ..models.post import Post

class PostResource(Resource):

  parser = reqparse.RequestParser().add_argument('before').add_argument('after')

  def get(self, id=None):
    args = self.parser.parse_args()
    if id:
      return self.get_by_id(id)
    elif args['before']:
      return self.get_before(args['before'])
    elif args['after']:
      return self.get_after(args['after'])
    else:
      return self.get_all()

  @marshal_with(pagination_fields(Post.fields))
  def get_all(self):
    return Post.query.order_by(Post._id.desc()).paginate(max_per_page=20)

  @marshal_with(pagination_fields(Post.fields))
  def get_before(self, id):
    return Post.query.order_by(Post._id.desc()).filter(Post._id <= id).paginate(max_per_page=20)

  @marshal_with(pagination_fields(Post.fields, reverse=True))
  def get_after(self, id):
    return Post.query.filter(Post._id >= id).paginate(max_per_page=20)

  @marshal_with(Post.fields)
  def get_by_id(self, id):
    return Post.query.get_or_404(id_decode(id))

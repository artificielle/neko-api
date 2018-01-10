from flask_restful import Resource, marshal
from ..models.post import Post

class PostResource(Resource):

  def get(self, id=None):
    return self.get_by_id(id) if id else self.get_all()

  def get_all(self):
    posts = Post.query.all()
    return {'data': marshal(posts, Post.fields), 'page_size': len(posts)}

  def get_by_id(self, id):
    post = Post.query.filter_by(id=id).first()
    return marshal(post, Post.fields) if post else None, 404

from sqlalchemy import Column, DateTime, Integer, String, Text
from flask_restful import fields
from ..common.util import id_encode
from . import db

class Post(db.Model):
  _id = Column(Integer, primary_key=True)
  time = Column(DateTime, nullable=False)
  link = Column(String, nullable=False, unique=True, index=True)
  site = Column(String, nullable=False)
  title = Column(String, nullable=False)
  author = Column(String, nullable=False)
  summary = Column(Text, nullable=False)
  # tags: List[str] = Column(Text)

  fields = {
    'id': fields.String(attribute=lambda x: id_encode(x._id)),
    'time': fields.DateTime('iso8601'),
    'link': fields.String,
    'site': fields.String,
    'title': fields.String,
    'author': fields.String,
    'summary': fields.String,
  }

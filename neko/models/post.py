from sqlalchemy import Column, DateTime, Integer, String, Text
from flask_restful import fields
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
    'id': fields.String(attribute='_id'),
    'time': fields.Integer(attribute=lambda x: x.time.timestamp()),
    'link': fields.String,
    'site': fields.String,
    'title': fields.String,
    'author': fields.String,
    'summary': fields.String,
  }

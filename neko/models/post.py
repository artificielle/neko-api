from sqlalchemy import Column, DateTime, Integer, String, Text
from flask_restful import fields
from . import db

class Post(db.Model):
  id = Column(Integer, primary_key=True)
  time = Column(DateTime)
  link = Column(String)
  site = Column(String)
  title = Column(String)
  author = Column(String)
  summary = Column(Text)
  # tags: List[str] = Column(Text)

  fields = {
    'id': fields.Integer,
    'time': fields.DateTime('iso8601'),
    'link': fields.String,
    'site': fields.String,
    'title': fields.String,
    'author': fields.String,
    'summary': fields.String,
  }

from typing import Type, List, NamedTuple

# <https://stackoverflow.com/questions/2166818>
def is_namedtuple(data):
  fields = getattr(type(data), '_fields', None)
  return (
    type(data).__bases__ == (tuple,) and
    isinstance(fields, tuple) and
    all(isinstance(field, str) for field in fields)
  )

# Fix marshal for namedtuple
def marshal_namedtuple(data, fields):
  from collections import OrderedDict
  def make(cls):
    return cls() if isinstance(cls, type) else cls
  if isinstance(data, (list, tuple)) and not is_namedtuple(data):
    return [marshal_namedtuple(d, fields) for d in data]
  return OrderedDict((k, make(v).output(k, data)) for k, v in fields.items())

def namedtuple_fields(nt: Type[NamedTuple]):
  from datetime import datetime
  from flask_restful import fields
  type_to_field = {
    str: fields.String(),
    int: fields.Integer(),
    float: fields.Float(),
    bool: fields.Boolean(),
    datetime: fields.DateTime('iso8601'),
    List[str]: fields.List(fields.String),
    List[int]: fields.List(fields.Integer),
    List[float]: fields.List(fields.Float),
  }
  return {k: type_to_field[t] for k, t in nt._field_types.items()}

def pagination_fields(item_fields, reverse=False):
  from flask_restful import fields
  data_attribute = (lambda x: x.items[::-1]) if reverse else 'items'
  return {
    'data': fields.List(fields.Nested(item_fields), attribute=data_attribute),
    'page': fields.Integer,
    'per_page': fields.Integer,
  }

def id_encode(data):
  return str(data)

def id_decode(data):
  return int(data)

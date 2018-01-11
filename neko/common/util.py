from typing import Type, List, NamedTuple

# <https://stackoverflow.com/questions/2166818>
def is_namedtuple(data):
  fields = getattr(type(data), '_fields', None)
  return (
    type(data).__bases__ == (tuple,) and
    isinstance(fields, tuple) and
    all(isinstance(field, str) for field in fields)
  )

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
  # pylint: disable = protected-access
  return {k: type_to_field[t] for k, t in nt._field_types.items()}

# Fix marshal for namedtuple
# <https://github.com/flask-restful/flask-restful/blob/master/flask_restful/__init__.py>
def marshal(data, fields):
  from collections import OrderedDict
  def make(cls):
    return cls() if isinstance(cls, type) else cls
  if isinstance(data, (list, tuple)) and not is_namedtuple(data):
    return [marshal(d, fields) for d in data]
  return OrderedDict((k, make(v).output(k, data)) for k, v in fields.items())

def hashid_encode(data):
  return data

def hashid_decode(data):
  return data

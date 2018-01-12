from unittest import TestCase

from typing import List, NamedTuple
from datetime import datetime
from collections import OrderedDict, namedtuple

from .util import is_namedtuple, marshal_namedtuple, namedtuple_fields

NT = namedtuple('NT', ['x', 'y'])

class TNT(NamedTuple):
  t: datetime = datetime.min
  x: str = ''
  xs: List[str] = []

class C(object):
  def __init__(self, t, x, xs):
    self.t = t
    self.x = x
    self.xs = xs

class UtilTestCase(TestCase):

  def test_is_namedtuple(self):
    self.assertTrue(is_namedtuple(TNT()))
    self.assertTrue(is_namedtuple(NT(1, 2)))

    self.assertFalse(is_namedtuple((1,)))
    self.assertFalse(is_namedtuple((1, 2)))

    self.assertFalse(is_namedtuple(None))
    self.assertFalse(is_namedtuple(True))
    self.assertFalse(is_namedtuple(10))
    self.assertFalse(is_namedtuple(''))

    self.assertFalse(is_namedtuple([]))
    self.assertFalse(is_namedtuple({}))
    self.assertFalse(is_namedtuple(C(t=datetime.min, x='a', xs=['b', 'c'])))

  def test_namedtuple_fields(self):
    from flask_restful import fields

    tnt_fields = namedtuple_fields(TNT)

    self.assertIsInstance(tnt_fields['t'], fields.DateTime)
    self.assertEqual(tnt_fields['t'].dt_format, 'iso8601')

    self.assertIsInstance(tnt_fields['x'], fields.String)

    self.assertIsInstance(tnt_fields['xs'], fields.List)
    self.assertIsInstance(tnt_fields['xs'].container, fields.String)

  def test_marshal_simple(self):
    from flask_restful import fields

    c_fields = {
      't': fields.DateTime('iso8601'),
      'x': fields.String,
      'xs': fields.List(fields.String),
    }

    c = C(
      t=datetime(year=2020, month=1, day=1, microsecond=1),
      x='a',
      xs=['b', 'c'],
    )

    expected = OrderedDict({
      't': '2020-01-01T00:00:00.000001',
      'x': 'a',
      'xs': ['b', 'c'],
    })

    self.assertDictEqual(expected, marshal_namedtuple(c, c_fields))

  def test_marshal_namedtuple(self):
    tnt_fields = namedtuple_fields(TNT)

    tnt = TNT(
      t=datetime(year=2020, month=1, day=1, microsecond=1),
      x='a',
      xs=['b', 'c'],
    )

    expected = OrderedDict({
      't': '2020-01-01T00:00:00.000001',
      'x': 'a',
      'xs': ['b', 'c'],
    })

    self.assertDictEqual(expected, marshal_namedtuple(tnt, tnt_fields))

from unittest import TestCase
import sympy as sym
import equations.plane_eqs as eq
from models.zone_axis import ZoneAxis

class TestPlaneEqs(TestCase):
  test_direction = ZoneAxis(1, 1, 0)

  def test_planes_ident(self):
    '''
    Test for planes identification
    '''
    h, k, L = sym.symbols('h k L')
    actual_expr = eq.planes_identification(self.test_direction)
    expect_expr = h + k
    self.assertEqual(sym.simplify(actual_expr - expect_expr), 0)
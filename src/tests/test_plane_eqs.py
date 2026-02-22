from unittest import TestCase
import equations.plane_eqs as eq
from models.zone_axis import ZoneAxis

class TestPlaneEqs(TestCase):
  test_direction = ZoneAxis(1, 1, 0)

  def test_planes_ident(self):
    '''
    Test for planes identification
    '''
    planes_range = eq.planes_identification(self.test_direction)
    self.assertIsNotNone(planes_range)
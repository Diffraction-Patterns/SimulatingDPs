from unittest import TestCase
import numpy as np
import equations.plane_eqs as eq
from models.zone_axis import ZoneAxis
from models.lattice import Lattice

class TestPlaneEqs(TestCase):
  def test_planes_ident(self):
    '''
    Test for planes identification
    '''
    test_direction = ZoneAxis(1, 1, 0)
    planes_range = eq.planes_identification(test_direction)
    self.assertIsNotNone(planes_range)

  def test_planes_length(self):
    '''
    Test for planes length calculation
    '''
    test_plane = (0, 0, 1)
    test_lattice = Lattice(3.852, 3.852, 3.723, 90.0, 90.0, 90.0)
    actual = eq.plane_vector_length(test_plane, eq.reciprocal_metric_tensor(test_lattice))
    expected = 0.268601
    np.testing.assert_allclose(actual, expected, rtol=1e-5)
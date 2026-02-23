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

  def test_two_shortest(self):
    '''
    Test for two shortest planes lengths
    '''
    test_zone_axis = ZoneAxis(1, 1, 0)
    test_lattice = Lattice(3.852, 3.852, 3.723, 90.0, 90.0, 90.0)
    test_planes = eq.planes_identification(test_zone_axis)
    actual_1, actual_2 = eq.two_shortest_planes(test_planes, test_lattice)
    expected_1 = (0, 0, -1)
    expected_2 = (-1, 1, 0)
    self.assertEqual(actual_1, expected_1)
    self.assertEqual(actual_2, expected_2)

  def test_plane_angle(self):
    '''
    Test for calculating plane angle
    '''
    test_zone_axis = ZoneAxis(1, 1, 0)
    test_lattice = Lattice(3.852, 3.852, 3.723, 90.0, 90.0, 90.0)
    test_planes = eq.planes_identification(test_zone_axis)
    h1, h2 = eq.two_shortest_planes(test_planes, test_lattice)
    g_star = eq.reciprocal_metric_tensor(test_lattice)
    actual = eq.plane_angles(h1, h2, g_star)
    expected = 90.0
    self.assertEqual(actual, expected)
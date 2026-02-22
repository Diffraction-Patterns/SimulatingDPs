import unittest
import numpy as np
import equations.equations as eq
from models.crystal_parameters import CrystalParameters

class TestEqs(unittest.TestCase):
  test_crystal = CrystalParameters(3.852, 3.852, 3.723, 90.0, 90.0, 90.0)

  def test_metric_tensor(self):
    '''
    Test for metric tensor function
    '''
    actual_mt = eq.metric_tensor(self.test_crystal)
    expected_mt = np.array([
      [14.8379, 0.0, 0.0],
      [0.0, 14.8379, 0.0],
      [0.0, 0.0, 13.8607]
    ])
    np.testing.assert_allclose(actual_mt, 
                               expected_mt, 
                               rtol=1e-5,
                               err_msg='compare reciprocal metric tensor')

  def test_reciprocal_metric_tensor(self):
    '''
    Test for metric tensor function
    '''
    actual_mt = eq.reciprocal_metric_tensor(self.test_crystal)
    expected_mt = np.array([
      [0.067395, 0.0, 0.0],
      [0.0, 0.067395, 0.0],
      [0.0, 0.0, 0.0721463]
    ])
    np.testing.assert_allclose(actual_mt, 
                               expected_mt, 
                               rtol=1e-5,
                               err_msg='compare reciprocal metric tensor')
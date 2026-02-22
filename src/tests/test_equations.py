import unittest
import numpy as np
import equations.equations as eq
from models.crystal_parameters import CrystalParameters

class TestEqs(unittest.TestCase):
  test_crystal = CrystalParameters(3.852, 3.852, 3.723, 90.0, 90.0, 90.0)

  def test_metric_tensor(self):
    actual_mt = eq.metric_tensor(self.test_crystal)
    expected_mt = np.array([
      [14.8379, 0.0, 0.0],
      [0.0, 14.8379, 0.0],
      [0.0, 0.0, 13.8607]
    ])
    print(actual_mt)
    self.assertTrue((actual_mt==expected_mt).all())
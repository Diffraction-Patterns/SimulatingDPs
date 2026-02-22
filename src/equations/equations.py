from models.crystal_parameters import CrystalParameters
from dataclasses import asdict
import numpy as np
from math import cos, sin, tan

'''
Equation for calculating the metric tensor
Returns:
  Matrix of metric tensor calculations
'''
def metric_tensor (c: CrystalParameters) -> np.array:
  r1c1 = c.a * c.a
  r1c2 = c.a * c.b * cos(c.gamma)
  r1c3 = c.a * c.c * cos(c.beta)

  r2c1 = c.b * c.a * cos(c.gamma)
  r2c2 = c.b * c.b
  r2c3 = c.b * c.c * cos(c.alpha)

  r3c1 = c.c * c.a * cos(c.beta)
  r3c2 = c.c * c.b * cos(c.alpha)
  r3c3 = c * c

  return np.array([r1c1, r1c2, r1c3],
                  [r2c1, r2c2, r2c3],
                  [r3c1, r3c2, r3c3])
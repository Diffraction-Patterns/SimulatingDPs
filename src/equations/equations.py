from models.crystal_parameters import CrystalParameters
from dataclasses import asdict
import numpy as np
from math import cos, sin, tan

def metric_tensor (c: CrystalParameters) -> np.array:
  '''
  Equation to calculate the metric tensor (g_triclinic)
  Parameters:
    CrystalParameters class
  Returns:
    Matrix of metric tensor calculations
  '''
  r1c1 = c.a**2
  r1c2 = c.a * c.b * cos(c.gamma)
  r1c3 = c.a * c.c * cos(c.beta)

  r2c1 = c.b * c.a * cos(c.gamma)
  r2c2 = c.b**2
  r2c3 = c.b * c.c * cos(c.alpha)

  r3c1 = c.c * c.a * cos(c.beta)
  r3c2 = c.c * c.b * cos(c.alpha)
  r3c3 = c**2

  return np.array([r1c1, r1c2, r1c3],
                  [r2c1, r2c2, r2c3],
                  [r3c1, r3c2, r3c3])

def reciprocal_metric_tensor (c: CrystalParameters) -> np.array:
  '''
  Equation to calculate the reciprocal metric tensor (g*_triclinic)
  Returns:
    Matrix of reciprocal metric tensor
  '''
  mt_matrix = np.array()
  return mt_matrix

def f_constant (alpha: float, beta: float, gamma: float) -> float:
  return (cos(alpha) * cos(beta)) - cos(gamma)

def unit_cell_volume_sq (c: CrystalParameters) -> float:
  '''
  Equation to calculate the squared volume of a unit cell
  '''
  a = (c.a**2) * (c.b**2) * (c.c**2)
  b = (1 
       - cos(c.alpha)**2 
       - cos(c.beta)**2 
       - cos(c.gamma)**2
       + 2*cos(c.alpha) * cos(c.beta) * cos(c.gamma))
  return a * b
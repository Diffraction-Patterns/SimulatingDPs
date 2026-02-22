from models.crystal_parameters import CrystalParameters
from dataclasses import asdict
import numpy as np
from math import cos, sin, radians

def metric_tensor (c: CrystalParameters) -> np.array:
  '''
  Equation to calculate the metric tensor (g_triclinic)
  Parameters:
    CrystalParameters class
  Returns:
    Matrix of metric tensor calculations
  '''
  r1c1 = c.a**2
  r1c2 = c.a * c.b * cos(radians(c.gamma))
  r1c3 = c.a * c.c * cos(radians(c.beta))

  r2c1 = c.b * c.a * cos(radians(c.gamma))
  r2c2 = c.b**2
  r2c3 = c.b * c.c * cos(radians(c.alpha))

  r3c1 = c.c * c.a * cos(radians(c.beta))
  r3c2 = c.c * c.b * cos(radians(c.alpha))
  r3c3 = c.c**2

  return np.array([[round(r1c1, 8), round(r1c2, 8), round(r1c3, 8)],
                  [round(r2c1, 8), round(r2c2, 8), round(r2c3, 8)],
                  [round(r3c1, 8), round(r3c2, 8), round(r3c3, 8)]], 
                  dtype=float)

def reciprocal_metric_tensor (c: CrystalParameters) -> np.array:
  '''
  Equation to calculate the reciprocal metric tensor (g*_triclinic)
  Returns:
    Matrix of reciprocal metric tensor
  '''
  r1c1 = (c.b**2) * (c.c**2) * (sin(radians(c.alpha))**2)
  r1c2 = c.a * c.b * c.c * f_constant(c.alpha, c.beta, c.gamma)
  r1c3 = c.a * (c.b**2) * c.c * f_constant(c.gamma, c.alpha, c.beta)

  r2c1 = c.a * c.b * (c.c**2) * f_constant(c.alpha, c.beta, c.gamma)
  r2c2 = (c.a**2) * (c.c**2) * (sin(radians(c.beta))**2)
  r2c3 = (c.a**2) * c.b * c.c * f_constant(c.beta, c.gamma, c.alpha)
  
  r3c1 = c.a * (c.b**2) * c.c * f_constant(c.gamma, c.alpha, c.beta)
  r3c2 = (c.a**2) * c.b * c.c * f_constant(c.beta, c.gamma, c.alpha)
  r3c3 = (c.a**2) * (c.b**2) * (sin(radians(c.gamma))**2)

  mt_matrix = np.array([[round(r1c1, 8), round(r1c2, 8), round(r1c3, 8)],
                        [round(r2c1, 8), round(r2c2, 8), round(r2c3, 8)],
                        [round(r3c1, 8), round(r3c2, 8), round(r3c3, 8)]], 
                        dtype=float)
  
  scalar_v = 1.0/(unit_cell_volume_sq(c))
  return scalar_v*mt_matrix

def f_constant (x: float, y: float, z: float) -> float:
  return round((cos(radians(x)) * cos(radians(y))) - cos(radians(z)), 2)

def unit_cell_volume_sq (c: CrystalParameters) -> float:
  '''
  Equation to calculate the squared volume of a unit cell
  '''
  a = (c.a**2) * (c.b**2) * (c.c**2)
  b = (1 
       - cos(radians(c.alpha))**2 
       - cos(radians(c.beta))**2 
       - cos(radians(c.gamma))**2
       + 2*cos(radians(c.alpha)) * cos(radians(c.beta)) * cos(radians(c.gamma)))
  return round(a * b, 8)
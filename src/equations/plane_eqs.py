import numpy as np
import math
from models.zone_axis import ZoneAxis
from models.lattice import Lattice
from equations.lattice_eqs import reciprocal_metric_tensor

def planes_identification(zad: ZoneAxis, maxRange: int = 5) -> list[np.array]:
  '''
  Computes the zone axis planes using the equation:
    hx + ky + Lz = 0
  Return:
    List of tuples representing points
  '''
  x, y, z = zad.x, zad.y, zad.z
  plane_directions = []

  for h in range(-maxRange, maxRange+1):
    for k in range(-maxRange, maxRange+1):
      for l in range(-maxRange, maxRange+1):
        if (h, k, l) == (0, 0, 0):
          continue
        if h*x + k*y + l*z == 0:
          plane_directions.append(np.array([h, k, l]))
  return plane_directions

def plane_vector_length(hkl: np.array, g_star: np.array) -> float:
  '''
  Calculates the magnitude of the given plane vector
  Parameters:
    hkl: vector(int, int, int) - represents a vector of the plane (h, k, L)
    g_star: np.array - matrix from calculating the reciprocal metric tensor
  Return:
    length of the given vector
  '''
  return float(np.sqrt(hkl @ g_star @ hkl)) # @ represents dot product (Python 3.5+)

def two_shortest_planes(planes: list[np.array], c: Lattice):
  '''
  Finds the two (unique) shortest planes
  Parameters:
    planes: list of (h, k, L)
    c: Lattice
  '''
  g_star = reciprocal_metric_tensor(c)
  sorted_planes = sorted(planes, key=lambda hkl: plane_vector_length(hkl, g_star))
  
  # Filter out duplicate planes (i.e. (0,0,1) and (0,0,-1))
  pl1 = sorted_planes[0]
  abs_pl1 = np.abs(pl1)

  for p in sorted_planes[1:]:
    if not np.array_equal(np.abs(p), abs_pl1):
      return pl1, p
  
  ## should never be hit
  return sorted_planes[0], sorted_planes[1]

def plane_angles(hkl_1: np.array, hkl_2: np.array, g_star: np.array) -> float:
  '''
  Calculates the angle between planes using the equation:
    cos(theta)12 = hkl1 dot g* dot hkl2 / gh1 * gh2
  Parameters:
    hkl1 - plane 1
    g_star - reciprocal metric tensor
    hkl2 - plane 2
  Returns:
    plane angle (in degrees)
  '''
  numerator = hkl_1 @ g_star @ hkl_2
  denominator = plane_vector_length(hkl_1, g_star) * plane_vector_length(hkl_2, g_star)
  cos_theta = numerator / denominator

  # safety for floating point precision
  cos_theta = max(-1.0, min(1.0, cos_theta))
  return math.degrees(math.acos(cos_theta))
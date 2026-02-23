import numpy as np
import math
from models.zone_axis import ZoneAxis
from models.lattice import Lattice
from equations.lattice_eqs import reciprocal_metric_tensor

def planes_identification(zad: ZoneAxis, maxRange: int = 10) -> list[tuple[int, int, int]]:
  '''
  Computes the zone axis planes using the equation:
    hx + ky +Lz = 0
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
          plane_directions.append((h, k, l))
  return plane_directions

def plane_vector_length(hkl: tuple[int, int, int], g_star: np.array) -> float:
  '''
  Calculates the magnitude of the given plane vector
  Parameters:
    hkl: tuple[int, int, int] - represents a vector of the plane (h, k, L)
    g_star: np.array - matrix from calculating the reciprocal metric tensor
  Return:
    length of the given vector
  '''
  plane = np.asarray(hkl, dtype=float)
  return float(np.sqrt(plane @ g_star @ plane)) # @ represents dot product (Python 3.5+)

def two_shortest_planes(planes: tuple[int, int, int], c: Lattice):
  g_star = reciprocal_metric_tensor(c)
  sorted_planes = sorted(planes, key=lambda hkl: plane_vector_length(hkl, g_star))
  
  # Filter out duplicate planes (i.e. (0,0,1) and (0,0,-1))
  pl1 = sorted_planes[0]
  abs_pl1 = tuple(abs(x) for x in pl1)

  for p in sorted_planes[1:]:
    if tuple(abs(x) for x in p) != abs_pl1:
      return pl1, p
  
  ## should never be hit
  return sorted_planes[0], sorted_planes[1]

def plane_angles(h1: tuple[int, int, int], h2: tuple[int, int, int], g_star: np.array) -> float:
  '''
  Calculates the angle between planes using the equation:
    cos(theta)12 = h1 dot g* dot h2 / gh1 * gh2
  Parameters:
    h1 - plane 1
    g_star - reciprocal metric tensor
    h2 - plane 2
  Returns:
    plane angle (in degrees)
  '''
  nu = h1 @ g_star @ h2
  de = plane_vector_length(h1, g_star) * plane_vector_length(h2, g_star)
  cos_theta = nu / de

  # safety for floating point precision
  cos_theta = max(-1.0, min(1.0, cos_theta))
  return math.degrees(math.acos(cos_theta))
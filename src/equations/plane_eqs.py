import numpy as np
from models.zone_axis import ZoneAxis
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

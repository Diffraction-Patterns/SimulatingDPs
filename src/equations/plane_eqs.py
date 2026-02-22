import sympy as sym
from models.zone_axis import ZoneAxis

def planes_identification (zad: ZoneAxis):
  '''
  Computes the Zone axis equation satisfaction:
    hx + ky +Lz = 0
  '''
  h, k, L = sym.symbols('h k L')
  x, y, z = zad.x, zad.y, zad.z
  expr = h*x + k*y + L*z
  return expr
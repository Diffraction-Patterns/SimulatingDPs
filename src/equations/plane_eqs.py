from models.zone_axis import ZoneAxis

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
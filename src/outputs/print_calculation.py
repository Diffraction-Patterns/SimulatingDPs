from eq_selection.eq_selector import equation_selection
from models.lattice import Lattice
from models.zone_axis import ZoneAxis
import equations.lattice_eqs as l_eqs
import equations.plane_eqs as p_eqs

def print_calculations(lattice: Lattice, zone_axis: ZoneAxis):
  print('\n| === Calculations ===|')
  print(f'Lattice Parameters: {lattice}')
  print(f'Zone Axis Direction: {zone_axis}')
  planes = p_eqs.planes_identification(zone_axis)
  s1, s2 = p_eqs.two_shortest_planes(planes, lattice)
  g_star = l_eqs.reciprocal_metric_tensor(lattice)
  s1_magnitude = p_eqs.plane_vector_magnitude(s1, g_star)
  s2_magnitude = p_eqs.plane_vector_magnitude(s2, g_star)
  print('\nTwo smallest planes:')
  print(f'1. {s1} - {s1_magnitude} \n2. {s2} - {s2_magnitude}')
  angle = p_eqs.plane_angles(s1, s2, g_star)
  print(f'\nPlanes angle - {angle}')



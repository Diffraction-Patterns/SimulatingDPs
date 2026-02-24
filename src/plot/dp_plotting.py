import matplotlib.pyplot as plt
import numpy as np
from models.lattice import Lattice
from models.zone_axis import ZoneAxis
import equations.lattice_eqs as l_eqs
import equations.plane_eqs as p_eqs

def diffraction_pattern_plot (lattice: Lattice, zone_axis: ZoneAxis):

  # calculates plane data
  planes = p_eqs.planes_identification(zone_axis)
  smallest_1, smallest_2 = p_eqs.two_shortest_planes(planes, lattice)
  smallest_planes = np.stack([smallest_1, smallest_2])

  # plot planes (3D scatter)
  fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
  
  for h, k, l in smallest_planes:
    ax.scatter([h], [k], [l], color='black', s=80)
    ax.text(h, k, l, f'({h}, {k}, {l})', fontsize=10)
  
  ax.view_init(elev=0, azim=45)
  
  plt.show()
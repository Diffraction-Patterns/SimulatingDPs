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
  
  planes_filtered = np.stack(
    [smallest_1, smallest_2]
    + [p for p in planes
     if not (np.array_equal(p, smallest_1)) or (np.array_equal(p, smallest_2))]
     )

  # plot planes (3D scatter)
  fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
  
  ax.scatter(0, 0, 0, color='black', s=5)
  ax.text(0, 0, 0, '000', fontsize=5)

  for h, k, l in planes_filtered:
    ax.scatter([h], [k], [l], color='black', s=5)
    ax.text(h, k, l, f'{h}{k}{l}', fontsize=5)


  ax.set_axis_off()
  ax.view_init(elev=0, azim=0)
  
  plt.show()
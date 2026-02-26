import matplotlib.pyplot as plt
import numpy as np
from models.lattice import Lattice
from models.zone_axis import ZoneAxis
import equations.lattice_eqs as l_eqs
import equations.plane_eqs as p_eqs

def diffraction_pattern_plot (lattice: Lattice, zone_axis: ZoneAxis, maxRange: int = 5):

  # calculates plane data
  g_star = l_eqs.reciprocal_metric_tensor(lattice)
  planes = p_eqs.planes_identification(zone_axis, maxRange)
  s1, s2 = p_eqs.two_shortest_planes(planes, lattice)
  
  # calculate two smallest magnitudes 
  g1 = p_eqs.plane_vector_magnitude(s1, g_star)
  g2 = p_eqs.plane_vector_magnitude(s2, g_star)

  p1 = np.array([0, g1])
  p2 = np.array([g2, 0])
  
  points = []
  for i in range(-maxRange, maxRange):
    for j in range(-maxRange, maxRange):
      points.append(i*p1 + j*p2)
  points = np.asarray(points)
  
  # plot planes (3D scatter)
  fig, ax = plt.subplots()
  ax.scatter(points[:, 0], points[:, 1], color='black', s=5)
  ax.text(0, 0, '(000)', fontsize=5)

  for n in points:
    ax.scatter(n[0], n[1], color='black', s=5)


  ax.set_axis_off()
  
  plt.show()
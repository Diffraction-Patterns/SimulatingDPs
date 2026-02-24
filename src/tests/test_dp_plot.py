from unittest import TestCase
import matplotlib.pyplot as plt
import numpy as np
from models.lattice import Lattice
from models.zone_axis import ZoneAxis
from plot.dp_plotting import diffraction_pattern_plot 

class TestDPPlot(TestCase):
  def test_plot(self):
    test_lattice = Lattice(3.852, 3.852, 3.723, 90.0, 90.0, 90.0)
    test_zone_axis = ZoneAxis(1, 1, 0)
    # (array([ 0,  0, -1]), array([-1,  1,  0]))

    diffraction_pattern_plot(test_lattice, test_zone_axis)
    self.assertTrue(True)
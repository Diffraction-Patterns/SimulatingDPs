from models.crystal_parameters import CrystalParameters
from dataclasses import asdict
import numpy as np
from math import cos, sin, tan

def metric_tensor (crystal: CrystalParameters) -> np.array:
  params = asdict(crystal)
  return np.array([0, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0])
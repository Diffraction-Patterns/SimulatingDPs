# Storage area for user inputted parameters
parameters = {
  "lattice": None,
  "zone_axis_direction": None,
  "maxRange": 5,
  "hkl": None,
  "g_star": None
}

def get_param(key):
  return parameters[key]

def set_param(key, value):
  parameters[key] = value
import equations.lattice_eqs as l_eq
import equations.plane_eqs as p_eq
from models.lattice import Lattice
from models.zone_axis import ZoneAxis

def validate_p_option(option: str) -> int:
  '''
  Validates user input for parent option 1. Lattice 2. Zone Axis Direction
  Parameters:
    option: str - user input # 1-2
  Returns:
    options as int
  '''

def validate_c_option(option: str) -> str:
  '''
  Validates user input for child option a-z for respective parent equation
  Parameters:
    option: str - user input character
  Returns:
    character
  '''

def equation_selection(p_option: str, c_option: str, lattice: Lattice, zone_axis: ZoneAxis, maxRange: int = 5):
  '''
  Selects the appropriate equation based on p and c options
  Parameters:
    p_option: str - parent option
    c_option: str - child option
    lattice - Lattice
    zone_axis - zone axis direction
  Returns:
    equation output
  '''
  p_op = validate_p_option(p_option)
  cc_op = validate_c_option(c_option) 
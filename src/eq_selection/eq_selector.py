import equations.lattice_eqs as l_eq
import equations.plane_eqs as p_eq
from eq_options import options
from params import parameters
from models.lattice import Lattice
from models.zone_axis import ZoneAxis
from processing import *

def execute_f_constant ():
  choice = input('New alpha, beta, and gamma? [y/n]: ').strip()
  if exit_prompt(choice):
    return None
  elif choice.lower() == 'y':
    a, b, c = prompt_abc()
    return l_eq.f_constant(a, b, c)
  elif choice.lower() == 'n':
    a, b, c = parameters['lattice'].a, parameters['lattice'].b, parameters['lattice'].c
    return l_eq.f_constant(a, b, c)
  else:
    print('Invalid option.')
    return None

def equation_selection(p_option: int, c_option: str):
  '''
  Selects the appropriate equation based on p and c options
  Parameters:
    p_option: int - parent option
    c_option: str - child option
    lattice - Lattice
    zone_axis - zone axis direction
  Returns:
    evaluated equation results
  '''
  selection = options[p_option]["children"][c_option]

  if selection == "f_constant":
    return execute_f_constant()
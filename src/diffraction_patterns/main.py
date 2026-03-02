from sys import exit
from params import (parameters, get_param, set_param)
from processing import (prompt_lattice, prompt_zone_axis_direction, prompt_options)
from outputs.print_calculation import print_calculations
# from eq_selection.eq_selector import equation_selection

def simTitle() -> None:
    print('|====== Diffraction Patterns Simulation ======|')

def main() -> int:
    simTitle()
    try:
      print('\n| === Lattice Parameters ===|')
      lattice_result = prompt_lattice()
      if lattice_result is None:
         return 0
      
      set_param("lattice", lattice_result)

      print('\n| === Zone Axis Direction ===|')
      zad_result = prompt_zone_axis_direction()
      if zad_result is None:
         return 0
      set_param("zone_axis_direction", zad_result)
      print_calculations(parameters['lattice'], parameters['zone_axis_direction'])

      # op_prompt = prompt_options()
      # if op_prompt is None:
      #    return 0
      # parent_selection, child_selection = op_prompt
      # equation_selection(parent_selection, child_selection)
    except KeyboardInterrupt:
       print ('\nExiting...')
       exit(0)
    return 0

if __name__ == '__main__':
    exit(main())
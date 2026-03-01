import sys
from params import (parameters, get_param, set_param)
from processing import (prompt_lattice, prompt_zone_axis_direction, prompt_options)
from eq_selection.eq_selector import equation_selection
import plot.dp_plotting as spl

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
      zad_prompt = prompt_zone_axis_direction()
      if zad_prompt is None:
         return 0
      set_param("zone_axis_direction", zad_prompt)

      op_prompt = prompt_options()
      if op_prompt is None:
         return 0
      parent_selection, child_selection = op_prompt
      equation_selection(parent_selection, child_selection)
    except KeyboardInterrupt:
       print ('\nExiting...')
       sys.exit(0)
    return 0

if __name__ == '__main__':
    sys.exit(main())
import shlex
import sys
from params import (parameters, get_param, set_param)
from processing.prompt_lattice import prompt_lattice
from processing.prompt_zone_axis import prompt_zone_axis_direction
import equations.plane_eqs as eq
import plot.dp_plotting as spl

def simTitle() -> None:
    print('|====== Diffraction Patterns Simulation ======|')

def main() -> int:
    simTitle()
    try:
      print('\n| === Lattice Parameters ===|')
      set_param("lattice", prompt_lattice())

      print('\n| === Zone Axis Direction ===|')
      set_param("zone_axis_direction", prompt_zone_axis_direction())

      print(parameters["lattice"])
      print(parameters["zone_axis_direction"])
    except KeyboardInterrupt:
       print ('\nExiting...')
       sys.exit(0)
    return 0

if __name__ == '__main__':
    sys.exit(main())
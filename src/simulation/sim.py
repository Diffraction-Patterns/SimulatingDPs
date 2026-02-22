import shlex
import sys
from processing.prompt_lattice import prompt_lattice
from processing.prompt_zone_axis import prompt_zone_axis_direction

def simTitle() -> None:
    print('|====== Diffraction Patterns Simulation ======|')

def main() -> int:
    simTitle()
    try:
      print('\n| === Lattice Parameters ===|')
      crystal_params = prompt_lattice()

      print('\n| === Zone Axis Direction ===|')
      zone_axis_direction = prompt_zone_axis_direction()
      
      if crystal_params != None:
        print(crystal_params)
      if zone_axis_direction != None:
         print(zone_axis_direction)
    except KeyboardInterrupt:
       print ('\nExiting...')
       sys.exit(0)
    return 0

if __name__ == '__main__':
    sys.exit(main())
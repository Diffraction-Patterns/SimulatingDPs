import shlex
import sys
from processing.parameter_handler import prompt_crystal, prompt_zone_axis_direction

def simTitle() -> None:
    print('|====== Diffraction Patterns Simulation ======|')

def main() -> int:
    simTitle()
    try:
      crystal_params = prompt_crystal()
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
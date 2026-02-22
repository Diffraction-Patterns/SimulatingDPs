import shlex
import sys
from processing.parameter_handler import prompt_crystal_input, prompt_zone_axis_direction_input

def simTitle() -> None:
    print('|====== Diffraction Patterns Simulation ======|')

def main() -> int:
    simTitle()
    try:
      crystal_params = prompt_crystal_input()
      zone_axis_direction = prompt_zone_axis_direction_input()
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
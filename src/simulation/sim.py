import shlex
import sys
from processing.parameter_handler import prompt_input

def simTitle() -> None:
    print('|====== Diffraction Patterns Simulation ======|')

def main() -> int:
    simTitle()
    try:
      crystal_params = prompt_input()
      if crystal_params != None:
        print(vars(crystal_params))    
    except KeyboardInterrupt:
       print ('\nExiting...')
       sys.exit(0)
    return 0

if __name__ == '__main__':
    sys.exit(main())
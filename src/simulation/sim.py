import shlex
import sys
from processing.parameter_handler import prompt_input

def simTitle() -> None:
    print('|====== Diffraction Patterns Simulation ======|')

def main() -> int:
    simTitle()
    crystal_params = prompt_input()
    return 0

if __name__ == '__main__':
    sys.exit(main())
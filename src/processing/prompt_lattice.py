from processing.prompt_exit import run_exit
from models.lattice import Lattice

def prompt_lattice() -> Lattice:
  '''
  Handles user inputs for crystal parameters.

  Prompts user for six floating point number parameter values:
  a, b, c, alpha, beta, and gamma

  Return: 
    Lattice An object populated with inputted parameters
  '''
  params = ['a', 'b', 'c', 'alpha', 'beta', 'gamma']
  print('Type "exit" to quit') 

  while True:
    value_inputs = {}
  
    for idx, p in enumerate(params, start=1):
      while True:
        raw_input = input(f'{idx}. Enter value for [{p}]: ').strip()

        run_exit(raw_input)
        
        try:
          value_inputs[p] = float(raw_input)
          break
        except ValueError:
          print('Please enter a valid number.\n')

    try:
      return Lattice(**value_inputs)
    except ValueError as e:
      print(f'Error with parameter: {e}')
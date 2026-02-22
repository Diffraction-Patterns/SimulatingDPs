from models.lattice_parameters import LatticeParameters
from models.zone_axis import ZoneAxis 

def prompt_lattice() -> LatticeParameters:
  '''
  Handles user inputs for crystal parameters.

  Prompts user for six floating point number parameter values:
  a, b, c, alpha, beta, and gamma

  Return: 
    LatticeParameters An object populated with inputted parameters
  '''
  params = ['a', 'b', 'c', 'alpha', 'beta', 'gamma']
  rp_space_key = 'reciprocal_space'
  print('Type "exit" to quit') 

  while True:
    value_inputs = {}
  
    for idx, p in enumerate(params, start=1):
      while True:
        raw_input = input(f'{idx}. Enter value for [{p}]: ').strip()

        if raw_input.lower() == 'exit':
          print("Exiting parameter input...")
          return None
        
        try:
          value_inputs[p] = float(raw_input)
          break
        except ValueError:
          print('Please enter a valid number.\n')

    while True:
      raw_input = input('Reciprocal space [y/n]: ').strip().lower() 

      if raw_input == 'exit':
        print("Exiting parameter input...")
        return None
      
      if raw_input in ('y', 'n'):
        if raw_input == 'y':
          print('Set reciprocal space...')
          value_inputs[rp_space_key] = True
        break
      else:
        print('Please enter only [y]es or [n]o.')

    try:
      return LatticeParameters(**value_inputs)
    except ValueError as e:
      print(f'Error with parameter: {e}')

def prompt_zone_axis_direction() -> ZoneAxis:
  '''
  Handles user inputs for zone access direction.

  Prompts user for three integer number parameter values:
  x, y, z

  Return: 
    ZoneAxis - An object representing the zone axis direction
  '''
  params = ['x', 'y', 'z']
  while True:
    value_inputs = {}
  
    for idx, p in enumerate(params, start=1):
      while True:
        raw_input = input(f'{idx}. Enter value for [{p}]: ').strip()

        if raw_input.lower() == 'exit':
          print("Exiting parameter input...")
          return None
        
        try:
          value_inputs[p] = int(raw_input)
          break
        except ValueError:
          print('\nPlease enter a valid integer number.')

    try:
      return ZoneAxis(**value_inputs)
    except ValueError as e:
      print(f'Error with parameter: {e}')
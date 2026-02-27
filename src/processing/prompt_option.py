def validate_p_option(option: str, n_options: int) -> bool:
  '''
  Validates user input for parent option 1. Lattice 2. Zone Axis Direction
  Parameters:
    option: str - user input 
    n_options: int - number of options available
  Returns:
    true if input is int
  '''

def validate_c_option(option: str) -> bool:
  '''
  Validates user input for child option a-z for respective parent equation
  Parameters:
    option: str - user input character
  Returns:
    true if character
  '''
  
def prompt_lattice() -> Lattice:
  '''
  Handles user inputs for crystal parameters.

  Prompts user for six floating point number parameter values:
  a, b, c, alpha, beta, and gamma

  Return: 
    Lattice An object populated with inputted parameters
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

    ''' (NOT IN USE. may be used for future purposes)
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
    '''
    try:
      return Lattice(**value_inputs)
    except ValueError as e:
      print(f'Error with parameter: {e}')
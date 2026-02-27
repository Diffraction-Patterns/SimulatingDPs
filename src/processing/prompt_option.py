def validate_p_option(option: str, n_options: int) -> bool:
  '''
  Validates user input for parent option 1. Lattice 2. Zone Axis Direction
  Parameters:
    option: str - user input 
    n_options: int - number of options available
  Returns:
    true if input is int
  '''
  if option.isdigit():
    op = int(option)
    return op > 0 and op <= n_options
  return False

def validate_c_option(option: str) -> bool:
  '''
  Validates user input for child option a-z for respective parent equation
  Parameters:
    option: str - user input character
  Returns:
    true if character
  '''
  return len(option) == 1 and str.isalpha(option)
  
# def prompt_option():
#   while True:
    #raw_input = input(f'{idx}. Enter value for [{p}]: ').strip()

        # if raw_input.lower() == 'exit':
        #   print("Exiting parameter input...")
        #   return None
        
        # try:
        #   value_inputs[p] = float(raw_input)
        #   break
        # except ValueError:
        #   print('Please enter a valid number.\n')
    
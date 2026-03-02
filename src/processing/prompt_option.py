from processing.prompt_exit import run_exit
from eq_options import options

def validate_p_option(option: str, n_options: int = 2) -> bool:
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
    return 1 <= op and op <= n_options
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
  
def prompt_options():
  print("\n| === Equation Set Selection === |")
  while True:
    # parent option
    for op, op_desc in options.items():
      print(f'{op}. {op_desc['label']}')

    while True:
      raw_input = input('Enter option (or "exit"): ').strip()
    
      run_exit(raw_input)
        
      if not validate_p_option(raw_input):
        print('Please enter a valid option')
        continue

      p_op = int(raw_input)
      parent = options[p_op]

      while True:
        # child option
        print(f"\nSelected: {parent['label']}")
        print("Choose an operation:")

        for func_op, func_name in parent['children'].items():
          print(f'{func_op}. {func_name}')

        raw_child = input('Enter sub-option (or "exit"): ').strip()

        run_exit(raw_child)
          
        if not validate_c_option(raw_child):
          print('Please enter a valid option')
          continue

        if raw_child not in parent['children']:
          print('Invalid option.')
          continue

        c_op = raw_child
        
        return p_op, c_op
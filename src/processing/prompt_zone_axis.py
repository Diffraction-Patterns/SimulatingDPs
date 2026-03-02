from processing.prompt_exit import run_exit
from models.zone_axis import ZoneAxis 

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
    print('Enter the zone axis direction as 3 integers (i.e. 123 for (1 2 3): ')
    raw_input = input().strip()

    run_exit(raw_input)

    # account for valid inputs without space or commas (i.e. )    
    if raw_input.isdigit() and len(raw_input) == 3:
      direction = [int(d) for d in raw_input]
    else:
      # account for valid inputs separated by comma (,) or space ( )
      input_d = raw_input.replace(',', ' ').split()

      if len(input_d) != 3:
         print('Invalid input. Please try again.')
         continue
      
      try:
          direction = [int(d) for d in input_d]
      except ValueError:
           print('\nPlease enter a valid integer number.')
           continue

    for idx, p in enumerate(params):
      value_inputs[p] = direction[idx]
    
    try:
      return ZoneAxis(**value_inputs)
    except ValueError as e:
      print(f'Error with parameter: {e}')
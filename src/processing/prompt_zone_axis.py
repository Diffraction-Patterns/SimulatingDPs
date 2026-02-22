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
from models.crystal_parameters import CrystalParameters

'''
Handles user inputs for parameters.

Prompts user for six floating point number parameter values:
a, b, c, alpha, beta, and gamma

Return: 
  CrystalParameters An object populated with inputted parameters
'''
def prompt_input() -> CrystalParameters:
  params = ['a', 'b', 'c', 'alpha', 'beta', 'gamma']
  print('Type "exit" to quit') 

  while True:
    value_inputs = {}
    param_i = 1
  
    for p in params:
      while True:
        raw_input = input(f'{param_i}. Enter value for [{p}]: ').strip()

        if (raw_input.lower() == 'exit'):
          print("Exiting parameter input...")
          return None
        
        try:
          value_inputs[p] = float(raw_input)
          param_i += 1
          break
        except ValueError:
          print('Please enter a valid number.\n')

    try:
      return CrystalParameters(**value_inputs)
    except ValueError as e:
      print(f'Error with parameter: {e}')

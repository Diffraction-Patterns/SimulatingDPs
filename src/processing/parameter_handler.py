from processing.crystal_parameters import CrystalParameters

'''
Handles user inputs for parameters.

Prompts user for six floating point number parameter values:
a, b, c, alpha, beta, and gamma

Return: 
  CrysParams: An object populated with inputted parameters
'''
def prompt_input() -> CrystalParameters:
  params = ['a', 'b', 'c', 'alpha', 'beta', 'gamma']

  while True:
    value_inputs = {}
    print('Type "exit" to quit') 
    for p in params:
      while True:
        print(f'Enter value for [{p}]')
        raw_input = input().strip()

        if (raw_input.lower() == 'exit'):
          print("Exiting parameter input...")
          return None
        
        try:
          value_inputs[p] = float(raw_input)
          break
        except ValueError:
          print('Please enter a valid number.\n')

    try:
      return CrystalParameters(**value_inputs)
    except ValueError as e:
      print(f'Error with parameter: {e}')

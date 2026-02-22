from CrysParams import CrysParams

'''
Handles user inputs for parameters.

Prompts user for six floating point number parameter values:
a, b, c, alpha, beta, and gamma

Return: 
  CrysParams: An object populated with inputted parameters
'''
def prompt_input() -> CrysParams:
  params = ['a', 'b', 'c', 'alpha', 'beta', 'gamma']

  while True:
    value_inputs = {}
    for p in params:
      while True:
        print(f'Enter value for [{p}]')
        print('Type "exit" to quit') 
        raw_input = input().strip()

        if (raw_input.lower() == 'exit'):
          print("Exiting parameter input...")
          return None
        
        try:
          value_inputs[p] = float(raw_input)
          break
        except ValueError:
          print('Please enter a valid number.')

    try:
      return CrysParams(**value_inputs)
    except ValueError as e:
      print(f'Error with parameter: {e}')

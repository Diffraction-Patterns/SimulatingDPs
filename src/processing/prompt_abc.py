from processing.prompt_exit import exit_prompt

def prompt_abc() -> list[float]:
  '''
  Handles user inputs for alpha, beta, gamma
  '''
  params = ['alpha', 'beta', 'gamma']
  while True:
    value_inputs = []

    for p in params:  
      while True:
        try:
          raw_input = input(f'Enter {p}: ').strip()
          value = float(raw_input)
          value_inputs.append(value)
          break
        except ValueError:
            print('\nPlease enter a valid number.')

    return value_inputs
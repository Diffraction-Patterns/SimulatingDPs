from sys import exit
def exit_prompt (s: str) -> bool:
  return s.lower() == 'exit'

def run_exit (s: str) -> None:
  if exit_prompt(s):
    exit(0)
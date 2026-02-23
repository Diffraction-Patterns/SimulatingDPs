from dataclasses import dataclass

@dataclass
class Lattice:
  '''
  Data Class to hold parameters of a lattice of a crystal
  '''
  a: float
  b: float
  c: float
  alpha: float
  beta: float
  gamma: float

  # denotes if reciprocal space should be used
  reciprocal_space: bool = False

  def __post_init__(self):
    self._validate_parameters()

  def _validate_parameters(self) -> None:
    numeric_parameters = ['a', 'b', 'c', 'alpha', 'beta', 'gamma']
    for name in numeric_parameters:
      value = getattr(self, name)
      if value <= 0.0:
        raise ValueError(f'{name} must be greater than 0.')
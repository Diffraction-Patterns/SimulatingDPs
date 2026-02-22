from dataclasses import dataclass

@dataclass
class CrysParams:
  a: float
  b: float
  c: float
  alpha: float
  beta: float
  gamma: float

  def __post_init__(self):
    self._validate_parameters()

  def _validate_parameters(self) -> None:
    for name, value in vars(self).items():
      if value <= 0.0:
        raise ValueError(f'{name} must be greater than 0.')
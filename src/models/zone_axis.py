from dataclasses import dataclass

@dataclass
class ZoneAxis:
  '''
  Data Class to hold direction for a Zone Axis
  '''
  x: int
  y: int
  z: int
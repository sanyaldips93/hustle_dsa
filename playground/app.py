from collections import deque
from typing import List, Tuple

def get_transformations(shape: List[Tuple[int, int]]):
  """Generate all 8 transformations (rotations and reflections)."""
  shapes = []
  for x, y in shape:
      shapes.append([
          (x, y), (y, x), (-x, y), (-y, x),
          (x, -y), (y, -x), (-x, -y), (-y, -x)
      ])
  return min([tuple(sorted(s)) for s in zip(*shapes)])


print(get_transformations([(2,3)]))
from collections import defaultdict

class LifeGrid:
  def __init__(self, pattern) -> None:
   self.pattern = pattern

  def evolve(self):
    neighbours = (
      (-1,-1), # Above left
      (-1,0), # Above
      (-1,1), # Above right
      (0,-1), # Left
      (0,1), # Right
      (1,-1), # Below left
      (1,0), # Below
      (1,1)  # Below right
    
    )
    num_neighbors = defaultdict(int)
    for row, cols in self.pattern.alive_cells:
      for drow, dcols in neighbours:
        num_neighbors = [(row + drow, cols + dcols)] += 1
    stay_alive = {
      cell for cell, num in num_neighbors.items() if num in {2,3}
    } & self.pattern.alive_cells
    come_alive = {
      cell for cell, num in num_neighbors.items() if num == 3
    } - self.pattern.alive_cells

  self.pattern.alive_cells = stay_alive | come_alive
  
    

  def as_string(self, bbox):
    pass

  def __str__(self):
    return (
      f"{self.pattern.name}\n"
      f"Alive cells -> {sorted(self.pattern.aliv_cells)}"
    )

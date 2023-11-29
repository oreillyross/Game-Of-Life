import curses
from pylife.patterns import Pattern
from pylife.grid import LifeGrid

__all__ = ["CursesView"]
class CursesView:
  def __init__(self, pattern: Pattern, gen=10, frame_rate=7, bbox=(0,0,20,20)):
    
    self.pattern = pattern
    self.gen = gen 
    self.frame_rate = frame_rate
    self.bbox = bbox

  def _draw(self, screen):
    current_grid = LifeGrid(self.pattern)
    curses.curs_set(0) 
    screen.clear()

    try:
      screen.addstr(0,0, current_grid.as_string(self.bbox))
    except curses.error:
      raise ValueError(f"Terminal is too small for pattern '{self.pattern.name}''")
      for _ in range(self.gen):
        current_grid.evolve()
        screen.addstr(0,0, current_grid.as_string(self.bbox))
        screen.refresh()
        sleep(1 / self.frame_rate)
      
  
  def show(self):
    curses.wrapper(self._draw)

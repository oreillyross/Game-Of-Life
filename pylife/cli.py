import argparse
from pylife import __version__, patterns, views

def get_command_line_args():
  parser = argparse.ArgumentParser(
    prog="pylife",
    description="Conways Game of Life right in your terminal!"
  )
  parser.add_argument(
    "-v", "--version", action="version", version=f"%(prog)s v{__version__}")
  parser.add_argument(
    "-p", "--pattern", 
    choices=[pat.name for pat in patterns.get_all_patterns()]                  ,
    default="Blinker",
    help="The pattern to take, (default: %(default)s"
  )
  parser.add_argument(
    "-a",
    "--all",
    action="store_true",
    help="Show all patterns in a sequence"
  )
  parser.add_argument(
    "--view",
    choices=views.__all__,
    default="CursesView",
    help="Display the life grid in a specific view (default: %(default)s"
  )
  parser.add_argument(
    "-g",
    "--gen",
    metavar="NUM_GENERATIONS",
    type=int,
    default=10,
    help="The number of generations to run (default: %(default)s)"
    
  )
  parser.add_argument(
    "f",
    "--fps",
    metavar="FRAMES_PER_SECOND",
    type=int,
    default=7,
    help="The number of frames per second (default: %(default)s)"
  )
  return parser.parse_args
from pylife.patterns import get_pattern
from pylife.views import CursesView

CursesView(get_pattern("Toad"), gen=100).show()
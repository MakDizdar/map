# Parser example
# Usage python parser_ex.py <data.osm>

import sys
from datetime import datetime

from osm_parser import get_default_parser
filename = sys.argv[1]
# The first argument after the PYTHON MODULE ON THE COMMANDLINE
# PARSE THE SUPPLIED OSM FILE
start = datetime.now()

parser = get_default_parser(filename)

edges = 0
for edge in parser.iter_ways():
    print(edge)
    edges += 1

end = datetime.now()

print("The data contains", edges, "edges/ways")
print("Parsing the date took", (end - start).total_seconds(), "seconds")

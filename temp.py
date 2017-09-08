from read_log import *
from graph import *

result = get_positions_array_from_file('output/4body.txt')
show_graph(result[0], result[1])
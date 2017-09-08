from read_log import *
from graph import *
from animation import *

result = get_positions_array_from_file('output/4body2.txt')
# show_graph(result[0], result[1])
show_animation(result[0], result[1])
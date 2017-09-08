from log import init_file
from body import Body
from physics.vector2 import Vector2

filepath = 'output/temp.txt'
bodies = [
        Body(Vector2(0, 0), Vector2(0, 0), 10),
        Body(Vector2(0, 0), Vector2(0, 0), 20),
        Body(Vector2(0, 0), Vector2(0, 0), 30)
]

init_file(filepath, bodies)
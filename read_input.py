from body import Body
from physics.vector2 import Vector2


"""Convert a string such as '1,1' into a vector object"""
def get_vector_from_string(str):
    split = str.split(',')
    return Vector2(float(split[0]), float(split[1]))


def get_bodies_from_file(file_path):
    bodies = []

    with open(file_path) as file:
        lines = file.readlines()

    # Remove trailing new line character
    lines = [line.strip() for line in lines]

    for line in lines:
        # A line looks like this:
        # 1,1|1,0|10e8
        # The first part is the starting position
        # The second part is the starting velocity
        # The third part is the mass
        split = line.split('|')
        position_string = split[0]
        velocity_string = split[1]
        position = get_vector_from_string(position_string)
        velocity = get_vector_from_string(velocity_string)
        mass = float(split[2])
        bodies.append(Body(position, velocity, mass))

    return bodies
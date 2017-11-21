from log import get_minimal_str_of_vector2
from physics.vector2 import Vector2
from body import Body
import random
import math


def get_mass():
    return 1.989e30


def get_distance_and_velocity():
    distance = 10e10
    velocity = 10e5
    return distance, velocity

def get_random_angle_rad():
    deg = random.randrange(0, 360, 1)
    return deg / 180 * math.pi


def generate_star(distance, velocity_magnitude, mass):
    random_angle = get_random_angle_rad()

    position = Vector2(0, 0)
    position.x = math.cos(random_angle) * distance
    position.y = math.sin(random_angle) * distance

    velocity = Vector2(0, 0)
    velocity.x = math.cos(random_angle) * velocity_magnitude
    velocity.y = math.sin(random_angle) * velocity_magnitude

    return Body(position, velocity, mass)


def generate_galaxy(number_of_stars):
    bodies = []

    for i in range(number_of_stars):
        distance_and_velocity = get_distance_and_velocity()
        star = generate_star(distance_and_velocity[0], distance_and_velocity[1], get_mass())
        bodies.append(star)

    return bodies


def write_to_file(bodies, file_path):
    with open(file_path, 'w+') as file:
        for body in bodies:
            position_string = get_minimal_str_of_vector2(body.position)
            velocity_string = get_minimal_str_of_vector2(body.velocity)
            mass_string = str(body.mass)
            string = '{}|{}|{}\n'.format(position_string, velocity_string, mass_string)
            file.write(string)


if __name__ == '__main__':
    print('How many stars do you want the galaxy to have?')
    amount = int(input())
    print('Generating solar system with {} stars'.format(amount))
    print('To what file do you want to output the generated galaxy?')
    file_path = 'output/' + input() + 'txt'

    bodies = generate_galaxy(amount)
    print(bodies)
    write_to_file(bodies, file_path)


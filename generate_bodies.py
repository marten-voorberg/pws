import random
import math
import matplotlib.pyplot as plt
from physics.vector2 import Vector2
from body import Body


def get_mass():
    return 1.989e30


def get_random_distance_to_center(min_distance_to_center = 0.5 * 10e9, max_distance_to_center = 10e9):
    distance_between = max_distance_to_center - min_distance_to_center
    step = distance_between / 1000
    distance_from_min = random.randrange(0, distance_between, step)
    return distance_from_min + min_distance_to_center


def get_random_angle():
    """"Returns a random angle between 0 and 2pi"""
    a = random.randrange(0, int(2 * math.pi * 100), 1)
    return a / 100


def calc_start_position(distance, angle):
    x = math.cos(angle) * distance
    y = math.sin(angle) * distance
    return Vector2(x, y)


def get_bodies(amount = 1000, center_position = Vector2(0, 0)):
    bodies = []
    for i in range(amount):
        mass = get_mass()
        distance = get_random_distance_to_center()
        angle = get_random_angle()
        start_pos = calc_start_position(distance, angle) + center_position
        bodies.append(Body(start_pos, Vector2(0, 0), mass))
    return bodies

if __name__ == '__main__':
    bodies = get_bodies(1000)
    x_array = []
    y_array = []
    for body in bodies:
        x_array.append(body.position.x)
        y_array.append(body.position.y)

    plt.scatter(x_array, y_array)
    plt.xlim(-10e9, 10e9)
    plt.ylim(-10e9, 10e9)
    plt.show()


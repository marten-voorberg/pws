from physics.vector2 import Vector2
from physics.random_angle import get_random_angle_rad
from physics.forces import calc_velocity_with_f_mpz
from body import Body
import random
import math
import matplotlib.pyplot as plt


def get_star_mass():
    return 1.989e30


def get_black_hole_mass():
    return 10e100


def get_random_distance():
    base = random.randrange(250, 1000, 10)
    return base * 10e10


def get_black_hole():
    # The black hole will always be in the center and will not be moving
    position = Vector2(0, 0)
    velocity = Vector2(0, 0)
    mass = get_black_hole_mass()
    return Body(position, velocity, mass)


def get_star():
    mass = get_star_mass()
    velocity = Vector2(0, 0)
    random_angle = get_random_angle_rad()
    distance = get_random_distance()

    position = Vector2(0, 0)
    position.x = math.cos(random_angle) * distance
    position.y = math.sin(random_angle) * distance

    return Body(position, velocity, mass)


def generate_system(star_amount):
    bodies = []

    black_hole = get_black_hole()
    bodies.append(black_hole)

    for i in range(star_amount):
        bodies.append(get_star())

    # Set starting velocities of stars
    for star in bodies:
        if star is not black_hole:
            vector_between_star_and_black_hole = star.position - black_hole.position
            distance = vector_between_star_and_black_hole.get_length()
            gravitational_force = star.get_gravitational_force_to(black_hole)
            gravitational_magnitude = gravitational_force.get_length()
            # print(gravitational_force)
            # print(star.mass)
            # print(distance)
            velocity_magnitude = calc_velocity_with_f_mpz(gravitational_magnitude, star.mass, distance)

            force_direction = vector_between_star_and_black_hole.get_unitvector()
            # The starting velocity will be perpendicular to the direction of the force
            velocity_direction = Vector2(-force_direction.y, force_direction.x)
            star.velocity = velocity_direction * velocity_magnitude

    return bodies

from body import Body
from physics.vector2 import Vector2
from log import get_minimal_str_of_vector2
import random
import math


def get_sun_mass():
    return 1.989e30


def get_planet_mass():
    return 5.972e24


def get_moon_mass():
    return 7.34e22


def get_stars(n):
    stars = []
    stars.append(Body(Vector2(0, 0), Vector2(0, 0), get_sun_mass()))
    return stars


def get_planets(n):
    planets = []
    for i in range(n):
        distance_to_center = random.randrange(50, 250) * 10e9
        position = Vector2(distance_to_center, 0)
        mass = get_planet_mass()
        planets.append(Body(position, Vector2(0, 0), mass))
    return planets


def write_to_file(bodies, file_path):
    with open(file_path, 'w+') as file:
        for body in bodies:
            position_string = get_minimal_str_of_vector2(body.position)
            velocity_string = get_minimal_str_of_vector2(body.velocity)
            mass_string = str(body.mass)
            string = '{}|{}|{}\n'.format(position_string, velocity_string, mass_string)
            file.write(string)


def generate_planet_system(n_stars = 1, n_planets = 3, n_moons = 0):
    bodies = []

    stars = get_stars(n_stars)
    for star in stars:
        bodies.append(star)

    planets = get_planets(n_planets)
    for planet in planets:
        planet.velocity(0, 10e9)
        bodies.append(planet)

    for body in bodies:
        body.set_resulting_gravitational_force(bodies)

    # for body in bodies:
    #     f_mpz_magnitude = body.resulting_force.get_length()
    #     f_mpz_direction = body.resulting_force.get_unitvector().rotate_90()
    #     velocity_magnitude = math.sqrt((f_mpz_magnitude * body.position.get_length()) / body.mass)
    #     body.velocity = f_mpz_direction * velocity_magnitude

    return bodies

if __name__ == '__main__':
    bodies = generate_planet_system()
    write_to_file(bodies, 'input/generated1.txt')

from body import Body
from physics.vector2 import Vector2
from physics.forces import calc_velocity_with_f_mpz
from log import get_minimal_str_of_vector2
from semi_randomizer import SemiRandomizer
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
    # stars.append(Body(Vector2(10e5, 0), Vector2(0, 0), get_sun_mass()))
    return stars


def get_random_angle_in_degrees():
    return random.randrange(0, 360, 1)


def get_distance_to_center(already_used_distances):
    distance_to_center = random.randrange(50, 1000, 150) * 10e9
    if distance_to_center in already_used_distances:
        return get_distance_to_center(already_used_distances)
    else:
        already_used_distances.append(distance_to_center)
        return distance_to_center


def get_planets(n, semi_randomizer):
    planets = []
    already_used_distances = []
    for i in range(n):
        # distance_to_center = random.randrange(50, 1000, 150) * 10e9
        distance_to_center = get_distance_to_center(already_used_distances)
        position = Vector2(distance_to_center, 0)
        mass = semi_randomizer.get_semi_random_mass()
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


def generate_system(n_stars = 1, n_planets = 5, n_moons = 0):
    planet_mass_semi_randomizer = SemiRandomizer('input/exoplanet_masses_kg.txt', 100)
    bodies = []

    stars = get_stars(n_stars)
    for star in stars:
        bodies.append(star)

    # planets = get_planets(n_planets, planet_mass_semi_randomizer)
    planets = [
        Body(Vector2(108e9, 0), Vector2(0, 0), 4.867e24),
        Body(Vector2(149.6e9, 0), Vector2(0, 0), 5.972e24),
        Body(Vector2(227e9, 0), Vector2(0, 0), 5.972e23),
        Body(Vector2(778.5e9, 0), Vector2(0, 0), 0.898e27),
        Body(Vector2(1.429e11, 0), Vector2(0, 0), 5.683e26)
    ]
    for planet in planets:
        bodies.append(planet)

    for body in bodies:
        body.set_resulting_gravitational_force(bodies)

    for body in bodies:
        force_to_stars = Vector2(0, 0)
        for star in stars:
            force_to_stars += body.get_gravitational_force_to(star)

        f_mpz_magnitude = force_to_stars.get_length()
        distance_to_center = body.position.get_length()
        velocity_magnitude = calc_velocity_with_f_mpz(f_mpz_magnitude, body.mass, distance_to_center)
        # velocity_magnitude = math.sqrt((f_mpz_magnitude * distance_to_center) / body.mass)
        # distance_to_center = body.position.get_length()
        # # f_mpz = m*v^2 / r
        # velocity_magnitude = math.sqrt((body.resulting_force.get_length() * distance_to_center) / body.mass)
        # # f_mpz_magnitude = body.resulting_force.get_length()
        body.velocity = Vector2(0, velocity_magnitude)

    # Rotate planets to a random degree
    for planet in planets:
        random_angle = get_random_angle_in_degrees()
        planet.position = planet.position.rotate_deg(random_angle)
        planet.velocity = planet.velocity.rotate_deg(random_angle)

    # for body in bodies:
    #     f_mpz_magnitude = body.resulting_force.get_length()
    #     f_mpz_direction = body.resulting_force.get_unitvector().rotate_90()
    #     velocity_magnitude = math.sqrt((f_mpz_magnitude * body.position.get_length()) / body.mass)
    #     body.velocity = f_mpz_direction * velocity_magnitude

    return bodies

if __name__ == '__main__':
    bodies = generate_system()
    write_to_file(bodies, 'input/generated100.txt')

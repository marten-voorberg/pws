from body import Body
from physics.vector2 import Vector2
from physics.forces import calc_velocity_with_f_mpz
from semi_randomizer import SemiRandomizer
import random


def get_stars(n):
    stars = [Body(Vector2(0, 0), Vector2(0, 0), 1.989e35)]
    # stars.append(Body(Vector2(0, 0), Vector2(0, 0), get_sun_mass()))
    # stars.append(Body(Vector2(10e5, 0), Vector2(0, 0), get_sun_mass()))
    return stars


def get_random_angle_in_degrees():
    return random.randrange(0, 360, 1)


def get_random_distance_to_center(already_used_distances):
    minimal_distance_between_planets = 50
    distance_to_center = random.randrange(50, 1000, minimal_distance_between_planets) * 10e9
    if distance_to_center in already_used_distances:
        return get_random_distance_to_center(already_used_distances)
    else:
        already_used_distances.append(distance_to_center)
        return distance_to_center


def get_planets(amount_planets, semi_randomizer):
    planets = []
    already_used_distances = []
    for i in range(amount_planets):
        distance_to_center = get_random_distance_to_center(already_used_distances)
        position = Vector2(distance_to_center, 0)
        mass = semi_randomizer.get_semi_random_mass()
        planets.append(Body(position, Vector2(0, 0), mass))
    return planets


def generate_system(n_stars = 1, n_planets = 5):
    planet_mass_semi_randomizer = SemiRandomizer('input/exoplanet_masses_kg.txt', 100)
    bodies = []

    stars = get_stars(n_stars)
    for star in stars:
        bodies.append(star)

    planets = get_planets(n_planets, planet_mass_semi_randomizer)
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
        body.velocity = Vector2(0, velocity_magnitude)

    # Rotate planets to a random degree
    for planet in planets:
        random_angle = get_random_angle_in_degrees()
        planet.position = planet.position.rotate_deg(random_angle)
        planet.velocity = planet.velocity.rotate_deg(random_angle)

    return bodies

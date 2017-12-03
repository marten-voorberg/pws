from body import Body
from physics.vector2 import Vector2
from physics.forces import calc_velocity_with_f_mpz
import random


def get_random_angle_in_degrees():
    return random.randrange(0, 360, 1)


def generate_system():
    bodies = []

    sun = Body(Vector2(0, 0), Vector2(0, 0), 1.989e30)
    bodies.append(sun)

    planets = [
        Body(Vector2(108e9, 0), Vector2(0, 0), 4.867e24),
        Body(Vector2(149.6e9, 0), Vector2(0, 0), 5.972e24),
        Body(Vector2(227e9, 0), Vector2(0, 0), 5.972e23),
        Body(Vector2(778.5e9, 0), Vector2(0, 0), 0.898e27),
        Body(Vector2(1.429e11, 0), Vector2(0, 0), 5.683e26)
    ]
    for planet in planets:
        bodies.append(planet)

    # Assign starting velocity to planets
    for planet in planets:
        force_to_stars = planet.get_gravitational_force_to(sun)
        f_mpz_magnitude = force_to_stars.get_length()
        distance_to_center = planet.position.get_length()
        velocity_magnitude = calc_velocity_with_f_mpz(f_mpz_magnitude, planet.mass, distance_to_center)
        planet.velocity = Vector2(0, velocity_magnitude)

    # Rotate planets to a random degree
    for planet in planets:
        random_angle = get_random_angle_in_degrees()
        planet.position = planet.position.rotate_deg(random_angle)
        planet.velocity = planet.velocity.rotate_deg(random_angle)

    return bodies

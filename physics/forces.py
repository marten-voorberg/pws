import physics.constants
import math


def calc_gravitational_force(mass1, mass2, distance):
    if distance == 0:
        return 0
    return physics.constants.G * mass1 * mass2 / distance ** 2


def calc_velocity_with_f_mpz(f_mpz, mass, distance):
    return math.sqrt((f_mpz * distance) / mass)

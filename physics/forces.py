import physics.constants


def calc_gravitational_force(mass1, mass2, distance):
    if distance == 0:
        return 0
    return physics.constants.G * mass1 * mass2 / distance ** 2

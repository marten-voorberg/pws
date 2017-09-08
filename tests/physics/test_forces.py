import unittest
from physics.forces import *


class TestGravitationalForce(unittest.TestCase):
    def test_standard(self):
        mass1 = 10e10
        mass2 = 10e10
        distance = 10e8
        expected = 6.67e-7
        actual = calc_gravitational_force(mass1, mass2, distance)
        self.assertAlmostEqual(expected, actual)

    def test_no_distance(self):
        mass1 = 1e10
        mass2 = 1e10
        distance = 0
        expected = 0
        actual = calc_gravitational_force(mass1, mass2, distance)
        self.assertAlmostEqual(actual, expected)


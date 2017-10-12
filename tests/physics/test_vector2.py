import unittest
import math
from physics.vector2 import Vector2


class TestVector2(unittest.TestCase):
    def test_init(self):
        x = 10
        y = 20
        actual = Vector2(x, y)
        self.assertTrue(actual.x == x and actual.y == y)

    def test_add(self):
        v1 = Vector2(2, 3)
        v2 = Vector2(3, 4)
        actual = v1 + v2
        expected = Vector2(5, 7)
        self.assertTrue(actual.x == expected.x and actual.y == expected.y)

    def test_sub(self):
        v1 = Vector2(2, 3)
        v2 = Vector2(3, 4)
        actual = v1 - v2
        expected = Vector2(-1, -1)
        self.assertTrue(actual.x == expected.x and actual.y == expected.y)

    def test_mul(self):
        v1 = Vector2(2, 3)
        x = 2
        actual = v1 * x
        expected = Vector2(4, 6)
        self.assertTrue(actual.x == expected.x and actual.y == expected.y)

    def test_true_div(self):
        v1 = Vector2(2, 3)
        x = 2
        actual = v1 / x
        expected = Vector2(1, 1.5)
        self.assertTrue(actual.x == expected.x and actual.y == expected.y)

    def test_get_length(self):
        v = Vector2(10, 20)
        actual = v.get_length()
        expected = 22.36067978
        self.assertAlmostEqual(actual, expected)

    def test_get_unit_vector(self):
        v = Vector2(5, 7)
        actual = v.get_unitvector()
        expected = Vector2(0.581238193, 0.813733471)
        self.assertTrue(expected.x - actual.x < 10e-5 and expected.y - actual.y < 10e-5 and actual.get_length() - 1 < 10e-5)

    def test_calc_distance_to(self):
        v1 = Vector2(3, 4)
        v2 = Vector2(4, 5)
        actual = v1.calc_distance_to(v2)
        expected = 1.41421356237
        self.assertAlmostEqual(actual, expected)

    def test_rotate_rad_1(self):
        v = Vector2(4, 0)
        actual = v.rotate_rad(0.5 * math.pi)
        expected = Vector2(0, 4)
        self.assertTrue(abs(actual.x - expected.x) < 10e-5 and abs(actual.y - expected.y) < 10e-5)

    def test_rotate_rad_2(self):
        v = Vector2(-4, -4)
        actual = v.rotate_rad(0.75 * math.pi)
        expected = Vector2(5.656854, 0)
        self.assertTrue(abs(actual.x - expected.x) < 10e-5 and abs(actual.y - expected.y) < 10e-5)

    def test_rotate_deg(self):
        v = Vector2(4, 0)
        actual = v.rotate_deg(90)
        expected = Vector2(0, 4)
        self.assertTrue(abs(actual.x - expected.x) < 10e-5 and abs(actual.y - expected.y) < 10e-5)

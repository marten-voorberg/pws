import unittest
from body import Body
from physics.vector2 import Vector2


class TestBody(unittest.TestCase):
    def test_init(self):
        pos = Vector2(1, 1)
        vel = Vector2(2, 2)
        mass = 100
        body = Body(pos, vel, mass)
        self.assertTrue(body.position is pos and body.velocity is vel and mass == body.mass)

    def test_update_position(self):
        pos = Vector2(5, 6)
        vel = Vector2(1, 1)
        body = Body(pos, vel, 1)
        dt = 0.1
        expected_x = 5.1
        expected_y = 6.1
        body.update_position(dt)
        self.assertTrue(expected_x - body.position.x < 10e-5 and expected_y - body.position.y < 10e-5)

    def test_update_velocity(self):
        force = Vector2(6, 4)
        dt = 0.1
        mass = 2
        position = Vector2(0, 0)
        velocity = Vector2(2, 2)
        body = Body(position, velocity, mass)
        body.resulting_force = force
        body.update_velocity(dt)
        expected_x = 2.3
        expected_y = 2.2
        self.assertTrue(expected_x - body.velocity.x < 10e-5 and expected_y - body.velocity.y < 10e-5)

    def test_get_gravitational_force_to(self):
        body = Body(Vector2(0, 0), Vector2(0, 0), 10e7)
        other_body = Body(Vector2(1, 0), Vector2(0, 0), 10e7)
        result = body.get_gravitational_force_to(other_body)
        expected_x = 66.7
        expected_y = 0
        self.assertTrue(expected_x - result.x < 10e-5 and expected_y - result.y < 10e-5)

    def test_set_resulting_gravitational_force(self):
        body1 = Body(Vector2(0, 0), Vector2(0, 0), 10e7)
        body2 = Body(Vector2(1, 0), Vector2(0, 0), 10e7)
        body3 = Body(Vector2(0, 1), Vector2(0, 0), 10e7)
        bodies = [body1, body2, body3]

        body1.set_resulting_gravitational_force(bodies)
        result = body1.resulting_force
        expected_x = 66.7
        expected_y = 66.7
        self.assertTrue(expected_x - result.x < 10e-5 and expected_y - result.y < 10e-5)
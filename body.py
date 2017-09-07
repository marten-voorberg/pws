from physics.vector2 import Vector2
from physics.forces import calc_gravitational_force


class Body:
    def __init__(self, position, velocity, mass):
        self.position = position
        self.velocity = velocity
        self.mass = mass

    def __repr__(self):
        return 'Body at {} with mass of {}kg'.format(self.position, self.mass)

    def update_position(self, dt):
        self.position += self.velocity * dt

    def update_velocity(self, resulting_force, dt):
        # F_res = m / a
        acceleration = resulting_force / self.mass
        delta_velocity = acceleration * dt
        self.velocity += delta_velocity

    def get_gravitational_force_to(self, other_body):
        vector_between = other_body.position - self.position
        distance_between = vector_between.get_length()

        direction_of_force = vector_between.get_unitvector()
        magnitude_of_force = calc_gravitational_force(self.mass, other_body.mass, distance_between)

        return direction_of_force * magnitude_of_force

    def set_resulting_gravitational_force(self, bodies):
        self.resulting_force = Vector2(0, 0)
        for body in bodies:
            if body is not self:
                self.resulting_force += self.get_gravitational_force_to(body)
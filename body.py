from physics.vector2 import Vector2
from physics.forces import calc_gravitational_force


class Body:
    def __init__(self, position, velocity, mass):
        self.position = position
        self.velocity = velocity
        self.mass = mass
        self.resulting_force = Vector2(0, 0)
        self.gravitational_force_from_other_bodies = {}

    def __repr__(self):
        return 'Body at {} with mass of {}kg'.format(self.position, self.mass)

    def update_position(self, dt):
        self.position += self.velocity * dt

    def update_velocity(self, dt):
        # F_res = m / a
        acceleration = self.resulting_force / self.mass
        delta_velocity = acceleration * dt
        self.velocity += delta_velocity

    def get_gravitational_force_to(self, other_body, other_body_index):
        if other_body_index in self.gravitational_force_from_other_bodies and False:
            return self.gravitational_force_from_other_bodies[other_body_index]
        else:
            vector_between = other_body.position - self.position
            distance_between = vector_between.get_length()

            direction_of_force = vector_between.get_unitvector()
            magnitude_of_force = calc_gravitational_force(self.mass, other_body.mass, distance_between)

            gravitational_force = direction_of_force * magnitude_of_force
            other_body.gravitational_force_from_other_bodies[other_body_index] = gravitational_force * -1
            return gravitational_force

    def set_resulting_gravitational_force(self, bodies):
        self.resulting_force = Vector2(0, 0)
        for i in range(len(bodies)):
            body = bodies[i]
            if body is not self:
                self.resulting_force += self.get_gravitational_force_to(body, i)
                self.gravitational_force_from_other_bodies = {}

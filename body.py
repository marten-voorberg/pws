from physics.vector2 import Vector2
from physics.forces import calc_gravitational_force

# Array
# class Body:
#     def __init__(self, position, velocity, mass):
#         self.position = position
#         self.velocity = velocity
#         self.mass = mass
#         self.resulting_force = Vector2(0, 0)
#         # Will be assigned later
#         self.index = None
#         self.calculated_bodies_indexes = []
#         self.resulting_force = Vector2(0, 0)
#
#     def __repr__(self):
#         return 'Body at {} with mass of {}kg'.format(self.position, self.mass)
#
#     def update_position(self, dt):
#         self.position += self.velocity * dt
#
#     def update_velocity(self, dt):
#         # F_res = m / a
#         acceleration = self.resulting_force / self.mass
#         delta_velocity = acceleration * dt
#         self.velocity += delta_velocity
#
#     def get_gravitational_force_to(self, other_body):
#         # if other_body.index not in self.calculated_bodies_indexes:
#         vector_between = other_body.position - self.position
#         distance_between = vector_between.get_length()
#
#         direction_of_force = vector_between.get_unitvector()
#         magnitude_of_force = calc_gravitational_force(self.mass, other_body.mass, distance_between)
#
#         gravitational_force = direction_of_force * magnitude_of_force
#         # print(gravitational_force)
#         # Add calculated gravitational force to 'the forces_to_other_body' dictionary for optimisation
#         other_body.resulting_force += gravitational_force
#         other_body.calculated_bodies_indexes.append(self.index)
#
#         return gravitational_force
#
#     def set_resulting_gravitational_force(self, bodies):
#         for body in bodies:
#             if body is not self and body.index not in self.calculated_bodies_indexes:
#                 f_g = self.get_gravitational_force_to(body)
#                 self.resulting_force += f_g
#         self.calculated_bodies_indexes = []


# Dictionary
class Body:
    def __init__(self, position, velocity, mass):
        self.position = position
        self.velocity = velocity
        self.mass = mass
        self.resulting_force = Vector2(0, 0)
        # The index of this dictionary will be the index of the other body in the body array
        # The content will be the force from that body
        self.forces_to_other_bodies = {}
        # Temporary value which will be replaced later
        self.index = -1

    def __repr__(self):
        return 'Body at {} with mass of {}kg'.format(self.position, self.mass)

    def update_position(self, dt):
        self.position += self.velocity * dt

    def update_velocity(self, dt):
        # F_res = m / a
        acceleration = self.resulting_force / self.mass
        delta_velocity = acceleration * dt
        self.velocity += delta_velocity

    def get_gravitational_force_to(self, other_body):
        if other_body.index in self.forces_to_other_bodies:
            return self.forces_to_other_bodies[other_body.index]
        else:
            vector_between = other_body.position - self.position
            distance_between = vector_between.get_length()

            direction_of_force = vector_between.get_unitvector()
            magnitude_of_force = calc_gravitational_force(self.mass, other_body.mass, distance_between)

            gravitational_force = direction_of_force * magnitude_of_force

            # Add calculated gravitational force to 'the forces_to_other_body' dictionary for optimisation
            other_body.forces_to_other_bodies[self.index] = gravitational_force * -1
            return gravitational_force

    def set_resulting_gravitational_force(self, bodies):
        self.resulting_force = Vector2(0, 0)
        for body in bodies:
            if body is not self:
                self.resulting_force += self.get_gravitational_force_to(body)
        # After we have calculated the resulting force the values in 'forces_to_other_bodies' have been
        # used and are now outdated so we clear the dictionary to save memory
        self.forces_to_other_bodies = {}

# Debugging
if __name__ == '__main__':
    body1 = Body(Vector2(0, 0), Vector2(0, 0), 10e20)
    body2 = Body(Vector2(10e10, 0), Vector2(0, 0), 10e20)


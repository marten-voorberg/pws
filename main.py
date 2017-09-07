import matplotlib.pyplot as plt
from body import Body
from physics.vector2 import Vector2

# dt = 1e10
#
# bodies = []

a = Body(Vector2(1, 1), Vector2(1, 0), 10e10)
b = Body(Vector2(-1, -1), Vector2(-1, 0), 10e10)
# c = Body(Vector2(1, -1), Vector2(0, 1), 10e10)
# d = Body(Vector2(-1, 1), Vector2(1, 0), 10e10)
a_x = []
a_y = []
b_x = []
b_y = []
# c_x = []
# c_y = []
# d_x = []
# d_y = []


# dt = 24 * 60 * 60
dt = 0.01
# simulated_time = dt * 100
simulated_time = 8
elapsed_time = 0
bodies = [a, b]

# sun = Body(Vector2(0, 0), Vector2(0, 0), 1.989e30)
# earth = Body(Vector2(149.6e9, 0), Vector2(0, 30e5), 5.972e24)
#
# bodies.append(sun)
# bodies.append(earth)
#
# xs = []
# ys = []

while elapsed_time < simulated_time:
    # Calculate the resulting gravitational force on each of the bodies and set this property
    for body in bodies:
        body.set_resulting_gravitational_force(bodies)

    # Update velocity and position based on the gravitational force calculated
    for body in bodies:
        body.update_velocity(body.resulting_force, dt)
        body.update_position(dt)

    # Debugging only
    a_x.append(a.position.x)
    a_y.append(a.position.y)
    b_x.append(b.position.x)
    b_y.append(b.position.y)
    # c_x.append(c.position.x)
    # c_y.append(c.position.y)
    # d_x.append(d.position.x)
    # d_y.append(d.position.y)

    # TODO: Write the positions of the objects to a file

    elapsed_time += dt

plt.plot(a_x, a_y, b_x, b_y)
# plt.plot(a_x, a_y, b_x, b_y, c_x, c_y, d_x, d_y)
plt.show()

# for i in range(500):
#     for i in range(len(bodies)):
#         body = bodies[i]
#         resulting_force = Vector2(0, 0)
#
#         for j in range(len(bodies)):
#             # Check if they are not the same body
#             if i != j:
#                 other_body = bodies[j]
#
#                 force = body.get_gravitational_force_to(other_body)
#
#                 # vector_between = other_body.position - body.position
#                 # distance_between = vector_between.get_length()
#                 # direction_of_force = vector_between.get_unitvector()
#                 #
#                 # magnitude_of_force = calc_gravitational_force(body.mass, other_body.mass, distance_between)
#                 # force_vector = direction_of_force * magnitude_of_force
#
#                 resulting_force += force
#
#         print(resulting_force)
#         body.update_velocity(resulting_force, dt)
#         body.update_position(dt)
#
#     xs.append(earth.position.x)
#     ys.append(earth.position.y)
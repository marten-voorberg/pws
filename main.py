import matplotlib.pyplot as plt
from body import Body
from physics.vector2 import Vector2
from physics.forces import calc_gravitational_force

# dt = 1e10
#
# bodies = []
#
# a = Body(Vector2(1, 1), Vector2(1, 0), 1e10)
# b = Body(Vector2(-1, -1), Vector2(-1, 0), 1e10)
#
# a_x = []
# a_y = []
# b_x = []
# b_y = []
#
# bodies.append(a)
# bodies.append(b)

dt = 24 * 60 * 60
bodies = []

sun = Body(Vector2(0, 0), Vector2(0, 0), 1.989e30)
earth = Body(Vector2(149.6e9, 0), Vector2(0, 30e8), 5.972e24)

bodies.append(sun)
bodies.append(earth)

xs = []
ys = []

for i in range(500):
    for i in range(len(bodies)):
        body = bodies[i]
        resulting_force = Vector2(0, 0)

        for j in range(len(bodies)):
            # Check if they are not the same body
            if i != j:
                other_body = bodies[j]

                force = body.get_gravitational_force_to(other_body)

                # vector_between = other_body.position - body.position
                # distance_between = vector_between.get_length()
                # direction_of_force = vector_between.get_unitvector()
                #
                # magnitude_of_force = calc_gravitational_force(body.mass, other_body.mass, distance_between)
                # force_vector = direction_of_force * magnitude_of_force

                resulting_force += force

        print(resulting_force)
        body.update_velocity(resulting_force, dt)
        body.update_position(dt)

    xs.append(earth.position.x)
    ys.append(earth.position.y)

plt.plot(xs, ys)
plt.show()

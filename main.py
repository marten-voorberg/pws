from body import Body
from physics.vector2 import Vector2
from log import *

# Animation and Graphs
import matplotlib.pyplot as plt
import matplotlib.animation as animation


a = Body(Vector2(1, 1), Vector2(1, 0), 10e10)
b = Body(Vector2(-1, -1), Vector2(-1, 0), 10e10)
a_x = []
a_y = []
b_x = []
b_y = []

file_path = 'output/temp.txt'
# dt = 24 * 60 * 60
dt = 0.1
# simulated_time = dt * 100
simulated_time = 30
elapsed_time = 0
bodies = [a, b]

# sun = Body(Vector2(0, 0), Vector2(0, 0), 1.989e30)
# earth = Body(Vector2(149.6e9, 0), Vector2(0, 30e5), 5.972e24)

# bodies.append(sun)
# bodies.append(earth)

init_file(file_path, bodies)
log_body_positions(file_path, bodies)

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

    log_body_positions(file_path, bodies)

    elapsed_time += dt

# plt.plot(a_x, a_y, b_x, b_y)
# # plt.plot(a_x, a_y, b_x, b_y, c_x, c_y, d_x, d_y)
# plt.show()

# Animation
# def _update_plot(i, fig, scat):
#     # scat.set_offsets(([0, i], [50, i], [100, i]))
#     scat.set_offsets(([a_x[i], a_y[i]], [b_x[i], b_y[i]]))
#     print('Frames: {}'.format(i))
#     return scat
#
# fig = plt.figure()
#
# x = [0, 50, 100]
# y = [0, 0, 0]
#
# ax = fig.add_subplot(111)
# ax.grid(True, linestyle = '-', color = '0.75')
# ax.set_xlim([-5, 5])
# ax.set_ylim([-5, 5])
#
# scat = plt.scatter(x, y, c = x)
# scat.set_alpha(0.8)
#
# anim = animation.FuncAnimation(fig, _update_plot, fargs = (fig, scat),
#                               frames = len(a_x), interval = 3)
#
# plt.show()
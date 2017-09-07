from physics.forces import calc_gravitational_force


distance = 149.6e9
mass1 = 1e30
mass2 = 1e24

print(calc_gravitational_force(mass1, mass2, distance))

# from physics.vector2 import Vector2
#
# a = Vector2(3, 4)
# b = Vector2(4, 5)
#
# print(a.calc_distance_to(b))
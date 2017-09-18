import math

def get_starting_v(mass, distance):
    G = 6.67e-11
    m_sun = 1.989e30
    F_G = (G * mass * m_sun) / (distance ** 2)
    v2 = F_G * distance / mass
    return math.sqrt(v2)

print('Venus: ' + str(get_starting_v(4.867e24, 108.2e9)))
print('Earth: ' + str(get_starting_v(5.972e24, 149.6e9)))
print('Mars: ' + str(get_starting_v(6.39e23, 227e9)))
print('Jupiter: ' + str(get_starting_v(1.989e27, 778.5e9)))
print('Saturn: ' + str(get_starting_v(5.683e26, 1.429e12)))

# 5.86e7,0|0,1504636|3.285e24

# 108.2e9,0|0,35016|4.867e24
# 149.6e9,0|0,29779|5.972e24
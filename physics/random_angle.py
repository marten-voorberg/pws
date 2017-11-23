import random, math

def get_random_angle_rad():
    deg = random.randrange(0, 360, 1)
    return deg / 180 * math.pi
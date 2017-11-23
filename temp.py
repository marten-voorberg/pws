import matplotlib.pyplot as plt
from generators.black_hole_system import generate_system

if __name__ == '__main__':
    stars = generate_system(1000)
    x_list = []
    y_list = []
    for star in stars:
        x_list.append(star.position.x)
        y_list.append(star.position.y)
    plt.plot(x_list, y_list, 'o')
    plt.show()
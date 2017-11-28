import matplotlib.pyplot as plt
from generators.black_hole_system import generate_system
from file_manipulation.input_file import write_bodies_to_input_file

if __name__ == '__main__':
    bodies = generate_system(100)
    file_path = 'input/generated_star_system3.txt'
    write_bodies_to_input_file(bodies, file_path)
    x_list = []
    y_list = []
    for star in bodies:
        x_list.append(star.position.x)
        y_list.append(star.position.y)
    plt.plot(x_list, y_list, 'o')
    # plt.show()

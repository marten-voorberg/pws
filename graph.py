import matplotlib.pyplot as plt
from read_log import get_positions_array_from_file
from plotting.distance_velocity import plot


def show_graph(x_list, y_list):
    amount_of_bodies = len(x_list)
    for i in range(amount_of_bodies):
        plt.plot(x_list[i], y_list[i])

    # plt.xlim(-10e8, 10e8)
    # plt.ylim(-10e8, 10e8)

    # plt.xlim(-300e9, 300e9)
    # plt.ylim(-300e9, 300e9)

    # plt.xlim(-6e7, 6e7)
    # plt.ylim(-5e6, 500000)
    # plt.xlim(-5, 5)
    # plt.ylim(-5, 5)
    # plt.xlim(-2.5, 2.5)
    # plt.ylim(-2.5, 2.5)
    plt.show()


def main():
    # file_path = 'output/generated_star_system2.txt'
    # x_and_y_lists = get_positions_array_from_file(file_path)
    # x_lists = x_and_y_lists[0]
    # y_lists = x_and_y_lists[1]
    # show_graph(x_lists, y_lists)

    plot('output/distance_velocity_2')

if __name__ == '__main__':
    main()

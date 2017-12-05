import matplotlib.pyplot as plt
from read_log import get_positions_array_from_file
from plotting.distance_velocity import plot


def show_graph(x_list, y_list):
    amount_of_bodies = len(x_list)
    for i in range(amount_of_bodies):
        plt.plot(x_list[i], y_list[i])

    # plt.xlim(-10e8, 10e8)
    # plt.ylim(-10e8, 10e8)

    # plt.xlim(-150e9, 150e9)
    # plt.ylim(-150e9, 150e9)

    # plt.xlim(140e9, 145e9)
    # plt.ylim(-10e5, 10e5)
    # plt.xlim(-5, 5)
    # plt.ylim(-5, 5)
    # plt.xlim(-2.5, 2.5)
    # plt.ylim(-2.5, 2.5)
    plt.show()


def main():
    file_path = 'output/black_hole_constant.txt'
    x_and_y_lists = get_positions_array_from_file(file_path)
    x_lists = x_and_y_lists[0]
    y_lists = x_and_y_lists[1]
    show_graph(x_lists[10:20], y_lists[10:20])
    # show_graph(x_lists, y_lists)

    # plot('output/distance_and_velocity_after.txt')

if __name__ == '__main__':
    main()

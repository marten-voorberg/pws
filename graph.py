import matplotlib.pyplot as plt

def show_graph(x_list, y_list):
    amount_of_bodies = len(x_list)
    for i in range(amount_of_bodies):
        plt.plot(x_list[i], y_list[i])
    # plt.ylim(-10e10, 10e10)
    # plt.xlim(-10e10, 10e10)
    # plt.xlim(-5, 5)
    # plt.ylim(-5, 5)
    plt.xlim(-2.5, 2.5)
    plt.ylim(-2.5, 2.5)
    plt.show()

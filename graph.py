import matplotlib.pyplot as plt

def show_graph(x_list, y_list):
    amount_of_bodies = len(x_list)
    for i in range(amount_of_bodies):
        plt.plot(x_list[i], y_list[i])
    plt.xlim(-1.5, 1.5)
    plt.ylim(-1.5, 1.5)
    plt.show()

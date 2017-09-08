import matplotlib.pyplot as plt
import matplotlib.animation as animation

def show_animation(x_list, y_list):
    my_list = []
    for i in range(len(x_list)):
        my_list.append([x_list[i], y_list[i]])

    def _update_plot(i, fig, scat):
        # scat.set_offsets((my_list))
        # scat.set_offsets(([a_x[i], a_y[i]], [b_x[i], b_y[i]]))
        # for j in range(len(x_list)):
        #     scat.set_offsets((x_list[j][i], y_list[j][i]))
        scat.set_offsets(([x_list[0][i], y_list[0][i]], [x_list[1][i], y_list[1][i]], [x_list[2][i], y_list[2][i]], [x_list[3][i], y_list[3][i]]))
        print('Frames: {}'.format(i))
        return scat

    fig = plt.figure()

    x = [0, 50, 100]
    y = [0, 0, 0]

    ax = fig.add_subplot(111)
    ax.grid(True, linestyle = '-', color = '0.75')
    ax.set_xlim([-5, 5])
    ax.set_ylim([-5, 5])

    scat = plt.scatter(x, y, c = x)
    scat.set_alpha(0.8)

    anim = animation.FuncAnimation(fig, _update_plot, fargs = (fig, scat),
                                  frames = len(x_list[0]), interval = 2)

    plt.show()
from log import *
from read_input import get_bodies_from_file
from read_log import get_positions_array_from_file
from graph import show_graph


def simulate(input_file_path, output_file_path, dt=0.01, simulated_time=10):
    bodies = get_bodies_from_file(input_file_path)
    elapsed_time = 0

    init_file(output_file_path, bodies)
    log_body_positions(output_file_path, bodies)

    while elapsed_time < simulated_time:
        # Calculate the resulting gravitational force on each of the bodies and set this property
        for body in bodies:
            body.set_resulting_gravitational_force(bodies)

        # Update velocity and position based on the gravitational force calculated
        for body in bodies:
            body.update_velocity(body.resulting_force, dt)
            body.update_position(dt)

        log_body_positions(output_file_path, bodies)

        elapsed_time += dt
        print('Seconds Simulated: {}'.format(elapsed_time))


def Main():
    input_file_path = 'input/2body.txt'
    output_file_path = 'output/2body.txt'

    simulate(input_file_path, output_file_path)

    x_and_y_lists = get_positions_array_from_file(output_file_path)
    x_lists = x_and_y_lists[0]
    y_lists = x_and_y_lists[1]
    show_graph(x_lists, y_lists)

if __name__ == '__main__':
    Main()
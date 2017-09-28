from log import *
from read_input import get_bodies_from_file
from read_log import get_positions_array_from_file
from graph import show_graph


def simulate(input_file_path, output_file_path, dt=0.01, simulated_time=10):
    print('Getting input from {}'.format(input_file_path))
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
            body.update_velocity(dt)
            body.update_position(dt)

        log_body_positions(output_file_path, bodies)

        elapsed_time += dt
        percentage = int(elapsed_time / simulated_time * 100)
        # print(bodies[1].velocity)
        print('Seconds Simulated: {}. {}% of calculations completed.'.format(elapsed_time, percentage))


def main():
    input_file_path = 'input/solarsystem2.txt'
    output_file_path = 'output/solarsystemA.txt'
    dt = 100000
    # simulated_time = dt * 433 * 2 + 1
    simulated_time = dt * 1000

    simulate(input_file_path, output_file_path, dt, simulated_time)

    x_and_y_lists = get_positions_array_from_file(output_file_path)
    x_lists = x_and_y_lists[0]
    y_lists = x_and_y_lists[1]
    show_graph(x_lists, y_lists)

if __name__ == '__main__':
    main()

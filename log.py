def get_minimal_str_of_vector2(vector):
    return '{},{}'.format(vector.x, vector.y)


def write_line(file, line):
    file.write(line + '\n')


def init_file(file_path, bodies):
    amount_of_bodies = len(bodies)

    with open(file_path, 'w+') as file:
        # file.write(str(amount_of_bodies) + '\n')
        write_line(file, str(amount_of_bodies))
        # file.write(str(amount_of_bodies) + '\n')

        for body in bodies:
            write_line(file, str(body.mass))


def log_body_positions(file_path, bodies):
    with open(file_path, 'a') as file:
        for body in bodies:
            write_line(file, get_minimal_str_of_vector2(body.position))
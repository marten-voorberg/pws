def write_bodies_to_input_file(bodies, file_path):
    with open(file_path, 'w+') as file:
        for body in bodies:
            position_string = body.position.get_minimal_string()
            velocity_string = body.velocity.get_minimal_string()
            mass_string = str(body.mass)
            string = '{}|{}|{}\n'.format(position_string, velocity_string, mass_string)
            file.write(string)
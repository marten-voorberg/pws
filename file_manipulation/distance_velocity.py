def write_distance_and_velocity_to_file(bodies, file_path):
    with open(file_path, 'w+') as file:
        for body in bodies:
            distance_to_center = body.position.get_length()
            velocity = body.velocity.get_length()
            string = '{}|{}\n'.format(distance_to_center, velocity)
            file.write(string)

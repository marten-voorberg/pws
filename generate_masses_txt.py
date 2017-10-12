if __name__ == '__main__':
    output_file_path = 'input/exoplanet_masses.txt'
    with open('input/planets.tab', 'r') as file:
        lines = file.readlines()
        for i in range(10, len(lines)):
            line = lines[i]
            split = line.split('\t')
            with open(output_file_path, 'a') as output_file:
                output_file.write(split[1] + '\n')

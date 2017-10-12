mass_jupiter = 1.898e27

if __name__ == '__main__':
    with open('input/exoplanet_masses_kg.txt', 'w+') as output_file:
        with open('input/exoplanet_masses_mj.txt', 'r') as input_file:
            lines = input_file.readlines()
            for line in lines:
                if not line == '\n':
                    stripped = line.strip()
                    mass_mj = float(stripped)
                    output_file.write('{}\n'.format(mass_mj * mass_jupiter))


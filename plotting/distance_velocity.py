import matplotlib.pyplot as plt

def plot(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    distances = []
    velocities = []
    for line in lines:
        split_string = line.split('|')
        distances.append(float(split_string[0]))
        velocities.append(float(split_string[1]))

    plt.plot(distances, velocities, 'o')
    plt.show()

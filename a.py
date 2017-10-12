import math
import matplotlib.pyplot as plt
# TODO: RENAME THIS FILE


def get_lowest_mass(masses):
    current_lowest = 10e99
    for mass in masses:
        if mass < current_lowest:
            current_lowest = mass
    return current_lowest


def get_highest_mass(masses):
    current_highest = -10e99
    for mass in masses:
        if mass > current_highest:
            current_highest = mass
    return current_highest


def f():
    amount_of_slices = 1000
    slice_index_and_occurrences = {}
    # Init dictionary
    # for i in range(amount_of_slices):
    #     slice_index_and_occurrences[i] = 0

    masses = []
    with open('input/exoplanet_masses.txt') as file:
        lines = file.readlines()
        for line in lines:
            # Some of our data may be incomplete, if so we want to simply ignore this data point
            if not line == '\n':
                masses.append(float(line))

    lowest_mass = get_lowest_mass(masses)
    highest_mass = get_highest_mass(masses)

    slice_size = (highest_mass - lowest_mass) / amount_of_slices

    for mass in masses:
        slice_index = math.floor((mass - lowest_mass) / slice_size)
        if slice_index in slice_index_and_occurrences:
            slice_index_and_occurrences[slice_index] += 1
        else:
            slice_index_and_occurrences[slice_index] = 1

    return slice_index_and_occurrences


if __name__ == '__main__':
    dict = f()
    value_array = []
    for key, value in dict.items():
        value_array.append(value)
    print()
    print(dict)

import math
import matplotlib.pyplot as plt
import random
# TODO: RENAME THIS FILE


class SemiRandomizer():
    def __init__(self, input_file_path, amount_of_slices=1000):
        self.amount_of_slices = amount_of_slices
        self.slice_index_and_occurrences = {}

        # Read the masses from the input file and append them to the array
        masses = []
        with open(input_file_path) as file:
            lines = file.readlines()
            for line in lines:
                # Some of our data may be incomplete,
                # If the data is incomplete there will be an empty line in the input file
                # We simply ignore the incomplete data
                if not line == '\n':
                    masses.append(float(line))

        self.highest_mass = -10e99
        self.lowest_mass = 10e99

        for mass in masses:
            if mass > self.highest_mass:
                self.highest_mass = mass
            if mass < self.lowest_mass:
                self.lowest_mass = mass

        self.amount_of_data_points = len(masses)

        # Calculate the slice size
        self.slice_size = (self.highest_mass - self.lowest_mass) / self.amount_of_slices

        # Determine how often masses in a certain slice occur
        # Add this information to the 'slice_index_and_occurrences' dictionary
        for mass in masses:
            slice_index = math.floor((mass - self.lowest_mass) / self.slice_size)
            if slice_index in self.slice_index_and_occurrences:
                self.slice_index_and_occurrences[slice_index] += 1
            # If the slice_index is not in the dictionary this is the first occurrence
            else:
                self.slice_index_and_occurrences[slice_index] = 1

    def get_semi_random_slice_index(self):
        random_number = random.randrange(0, self.amount_of_data_points)
        counter = 0
        # print(random_number)
        for key, value in self.slice_index_and_occurrences.items():
            counter += value
            if random_number < counter:
                return key

    def get_mass(self, slice_index):
        return self.lowest_mass + (slice_index + 0.5) * self.slice_size

    def get_semi_random_mass(self):
        slice_index = self.get_semi_random_slice_index()
        return self.get_mass(slice_index)

if __name__ == '__main__':
    sr = SemiRandomizer('input/simple.txt', 3)
    # print(sr.get_mass(1))
    temp_dict = {}
    for i in range(100000):
        j = sr.get_semi_random_mass()
        if j not in temp_dict:
            temp_dict[j] = 1
        else:
            temp_dict[j] += 1
    print(temp_dict)

# def get_lowest_mass(masses):
#     current_lowest = 10e99
#     for mass in masses:
#         if mass < current_lowest:
#             current_lowest = mass
#     return current_lowest
#
#
# def get_highest_mass(masses):
#     current_highest = -10e99
#     for mass in masses:
#         if mass > current_highest:
#             current_highest = mass
#     return current_highest
#
#
# def f(file_path, amount_of_slices=1000):
#     slice_index_and_occurrences = {}
#     # Init dictionary
#     # for i in range(amount_of_slices):
#     #     slice_index_and_occurrences[i] = 0
#     masses = []
#     with open(file_path) as file:
#         lines = file.readlines()
#         for line in lines:
#             # Some of our data may be incomplete, if so we want to simply ignore this data point
#             if not line == '\n':
#                 masses.append(float(line))
#
#     lowest_mass = get_lowest_mass(masses)
#     highest_mass = get_highest_mass(masses)
#     # print('highest_mass: {}'.format(highest_mass))
#     # print('lowest_mass: {}'.format(lowest_mass))
#     slice_size = (highest_mass - lowest_mass) / amount_of_slices
#     # print('slice_size: {}'.format(slice_size))
#     for mass in masses:
#         # print((mass - lowest_mass) / slice_size)
#         slice_index = math.floor((mass - lowest_mass) / slice_size)
#         # print('{}-{}'.format(mass, slice_index))
#         if slice_index in slice_index_and_occurrences:
#             slice_index_and_occurrences[slice_index] += 1
#         else:
#             slice_index_and_occurrences[slice_index] = 1
#
#     return slice_index_and_occurrences
#
#
# def get_semi_random_index(dict):
#     amount_of_data_points = 0
#     for key, value in dict.items():
#         amount_of_data_points += value
#
#     for i in range(0, 1):
#         random_number = random.randrange(0, amount_of_data_points)
#         counter = 0
#         # print(random_number)
#         for key, value in dict.items():
#             counter += value
#             if random_number < counter:
#                 return key
#
# if __name__ == '__main__':
#     # dict = f('input/exoplanet_masses.txt')
#     dict = f('input/simple.txt', 3)
#
#     temp_dict = {}
#     for i in range(10000):
#         j = get_semi_random_index(dict)
#         if j not in temp_dict:
#             temp_dict[j] = 1
#         else:
#             temp_dict[j] += 1
#     print(temp_dict)

    # amount_of_data_points = 0
    # for key, value in dict.items():
    #     amount_of_data_points += value

    # for i in range(0, 1):
    #     random_number = random.randrange(0, amount_of_data_points)
    #     print(random_number)
    #     for key, value in dict.items():
    #         if random_number < value:
    #             print(key)
    #             break

    # print(dict)

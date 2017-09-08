# DEPRECATED
# def get_positions_array_from_filed(file_path):
#     positions = []
#     with open(file_path, 'r') as file:
#         lines = file.readlines()
#
#     lines = [line.strip() for line in lines]
#
#     # The first line of a log file is the number of bodies
#     amount_of_bodies = int(lines[0])
#     print(amount_of_bodies)
#
#     for i in range(amount_of_bodies):
#         positions.append([])
#
#     index_of_current_body = 0
#
#     for j in range(1 + amount_of_bodies, len(lines)):
#         current_line = lines[j]
#         split_line = current_line.split(',')
#         x, y = float(split_line[0]), (split_line[1])
#         positions[index_of_current_body].append([x, y])
#
#         index_of_current_body += 1
#         if index_of_current_body >= amount_of_bodies:
#             index_of_current_body = 0
#
#     print(positions)
#     return positions


def get_positions_array_from_file(file_path):
    x_list = []
    y_list = []
    with open(file_path, 'r') as file:
        lines = file.readlines()

    lines = [line.strip() for line in lines]

    # The first line of a log file is the number of bodies
    amount_of_bodies = int(lines[0])

    for i in range(amount_of_bodies):
        x_list.append([])
        y_list.append([])

    index_of_current_body = 0

    for j in range(1 + amount_of_bodies, len(lines)):
        current_line = lines[j]
        split_line = current_line.split(',')
        x, y = float(split_line[0]), (split_line[1])
        x_list[index_of_current_body].append(x)
        y_list[index_of_current_body].append(y)

        index_of_current_body += 1
        if index_of_current_body >= amount_of_bodies:
            index_of_current_body = 0

    return x_list, y_list

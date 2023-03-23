def get_points_input_from_user():
    """"Function returns a nested lists of points.
     Example: [[1,1], [2,2], [3,3]]"""
    points = []
    number_of_points = int(input('Enter the amount of point to be entered: '))

    for i in range(0, number_of_points):
        x = int(input(f'x[{i}]= '))
        y = int(input(f'y[{i}]= '))
        points.append([x, y])

    return points


def get_geometric_transform():
    option = 0
    print("Geometric transform menu:"
          "\n1-Translação"
          "\n2-Escala"
          "\n3-Rotação"
          "\n4-Cisalhamento"
          "\n5-Reflexão")
    option_string = input('Enter the number correspondent to the geometric: ')
    if option_string.isnumeric():
        option = int(option_string)
    else:
        exit()
    return option

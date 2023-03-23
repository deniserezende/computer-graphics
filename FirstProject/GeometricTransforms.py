import logging
import numpy as np


# Translação
def translation(x, y, Tx, Ty):
    """"The translation function takes in four arguments: x, y, Tx, and Ty. It returns a new
    list of coordinates that have been translated by Tx and Ty in the x and y directions, respectively."""
    return [x + Tx, y + Ty]


# Escala
def scale(x, y, Sx, Sy):
    """The scale function takes in four arguments: x, y, Sx, and Sy.
    It returns a new list of coordinates that have been scaled by Sx and Sy in the x and y directions, respectively."""
    return [x * Sx, y * Sy]


# Rotação
def rotation(x, y, angle):
    """"The rotation function takes in three arguments: x, y, and angle.
    It returns a new list of coordinates that have been rotated by the specified angle around the origin."""
    # Define a matrix for rotation
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle), 0],
                                [np.sin(angle), np.cos(angle), 0],
                                [0, 0, 1]])

    # Define a list of coordinates
    coordinates = [x, y, 1]

    # Multiply the rotation matrix by the coordinates
    result_matrix = np.dot(rotation_matrix, coordinates)

    # Return the result of the matrix multiplication
    return result_matrix


# Cisalhamento
def shear(x, y, Kx, Ky):
    """In portuguese: cisalhamento.
    Performs a shear transformation on the point (x,y) given the shear factors Kx and Ky.
    The transformed point (new_x, new_y) is returned."""
    new_x = x + Kx * y
    new_y = y + Ky * x
    return [new_x, new_y]


# Reflexão
def reflection(x, y, r_type):
    """"This is a function that performs different types of reflections on a 2D point given as (x, y) coordinates.
    The type of reflection is specified by the parameter "r_type", which must be a string equal to 'x', 'y', 'y=x', or
    'y=-x'. Depending on the type of reflection, the function returns the new coordinates of the reflected point.
    If an invalid type is passed, the function logs an error message and returns [0, 0]."""
    new_x = 0
    new_y = 0
    match r_type:
        case 'x':
            new_x = x
            new_y = -y
        case 'y':
            new_x = -x
            new_y = y
        case 'y=x':
            new_x = y
            new_y = x
        case 'y=-x':
            new_x = -y
            new_y = -x
        case other:
            logging.error(f'The type entered is not valid: {r_type}.')

    return [new_x, new_y]


# Rotação em relação a um ponto P
def rotate_with_reference_point(x, y, theta, px, py):
    """Rotate a point (x,y) considering a reference point (px, py) by an angle of theta."""
    # Translation matrix to move point to the origin
    translation_matrix = np.array([[1, 0, px],
                                   [0, 1, py],
                                   [0, 0, 1]])

    # Rotation matrix to rotate the point
    rotation_matrix = np.array([[np.cos(theta), -np.sin(theta), 0],
                                [np.sin(theta), np.cos(theta), 0],
                                [0, 0, 1]])

    # Inverse translation matrix to move point back to original position
    inverse_translation_matrix = np.array([[1, 0, -px],
                                           [0, 1, -py],
                                           [0, 0, 1]])

    # Coordinates of the point
    coordinates = [x, y, 1]

    # Composite transformation matrix
    temp = np.dot(rotation_matrix, inverse_translation_matrix)
    composite_matrix = np.dot(translation_matrix, temp)

    # Apply transformation to the point
    result_matrix = np.dot(composite_matrix, coordinates)

    return result_matrix


# Escala em relação a um ponto P.
def scale_with_reference_point(x, y, Sx, Sy, px, py):
    """Scale a point (x,y) considering a reference point (px, py) by the factors Sx and Sy."""
    # Translation matrix to move point to the origin
    translation_matrix = np.array([[1, 0, px],
                                   [0, 1, py],
                                   [0, 0, 1]])

    # Scale matrix to scale the point
    scale_matrix = np.array([[Sx, 0, 0],
                            [0, Sy, 0],
                            [0, 0, 1]])

    # Inverse translation matrix to move point back to original position
    inverse_translation_matrix = np.array([[1, 0, -px],
                                           [0, 1, -py],
                                           [0, 0, 1]])

    # Coordinates of the point
    coordinates = [x, y, 1]

    # Composite transformation matrix
    composite_matrix = np.dot(translation_matrix, np.dot(scale_matrix, inverse_translation_matrix))

    # Apply transformation to the point
    result_matrix = np.dot(composite_matrix, coordinates)

    return result_matrix


# Escala em relação ao centro geométrico do objeto.
def scale_with_reference_point_as_geometric_center(x, y, Sx, Sy, cgx, cgy):
    return scale_with_reference_point(x, y, Sx, Sy, cgx, cgy)

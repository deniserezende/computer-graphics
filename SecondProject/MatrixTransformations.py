import logging
import numpy as np
import matplotlib.pyplot as plt


# DDA
def dda(x_initial, y_initial, x_final, y_final):
    """"The Digital Difference Analyzer (DDA) algorithm is used to draw lines on a screen in an incrementally."""
    logging.getLogger().setLevel(logging.INFO)

    # Calculate delta
    delta_x = x_final-x_initial
    delta_y = y_final-y_initial

    # Calculate step
    step = max(np.abs(delta_x), np.abs(delta_y))
    logging.info(f'step={step}')

    # Calculate increment in x and y
    x_inc = delta_x / step
    y_inc = delta_y / step

    # Plot points
    y = y_initial
    x = x_initial
    while x < x_final:
        plt.scatter(x=round(x), y=round(y), s=100, color='black')
        y = y + y_inc
        x = x + x_inc

    plt.show()


# Bresenham's line algorithm
def bresenhams_line_algorithm(x_initial, y_initial, x_final, y_final):
    """"Bresenham's line algorithm is a line drawing algorithm that determines the points of an n-dimensional raster
    that should be selected in order to form a close approximation to a straight line between two points."""
    logging.getLogger().setLevel(logging.INFO)

    # Calculate delta
    delta_x = x_final - x_initial
    delta_y = y_final - x_initial

    # Check direction to calculate increment in x and y
    x_inc = 0
    y_inc = 0
    match x_final > x_initial:
        case True:
            x_inc = 1
        case False:
            x_inc = -1

    match y_final > y_initial:
        case True:
            y_inc = 1
        case False:
            y_inc = -1

    logging.info(f'x_inc={x_inc}')
    logging.info(f'y_inc={y_inc}')

    # Check octant and call function
    if delta_x >= delta_y:
        _bla_first_octant(delta_x, delta_y, x_initial, y_initial, x_final, x_inc, y_inc)
    else:
        _bla_second_octant(delta_x, delta_y, x_initial, y_initial, y_final, x_inc, y_inc)
    plt.show()


def _bla_first_octant(delta_x, delta_y, x_initial, y_initial, x_final, x_inc, y_inc):
    p = 2 * abs(delta_y) - abs(delta_x)
    p2 = 2 * abs(delta_y)
    xy2 = 2 * (abs(delta_y) - abs(delta_x))
    # Plot points
    y = y_initial
    x = x_initial
    while x != x_final:
        x += x_inc

        if p < 0:
            p += p2
        else:
            p += xy2
            y += y_inc

        plt.scatter(x=round(x), y=round(y), s=100, color='black')


def _bla_second_octant(delta_x, delta_y, x_initial, y_initial, y_final, x_inc, y_inc):
    p = 2 * abs(delta_x) - abs(delta_y)
    p2 = 2 * abs(delta_x)
    xy2 = 2 * (abs(delta_x) - abs(delta_y))

    # Plot points
    y = y_initial
    x = x_initial
    while y != y_final:
        y += y_inc

        if p < 0:
            p += p2
        else:
            p += xy2
            x += x_inc

        plt.scatter(x=round(x), y=round(y), s=170, color='black')


# Bresenham's circle algorithm
def bresenhams_circle_algorithm(radius):
    """"Bresenham Algorithm is used to reduce the calculation needed for drawing a circle by making use of
    property of symmetry."""
    logging.getLogger().setLevel(logging.INFO)

    x = 0
    y = radius
    p = 1 - radius
    while x < y:
        # Step7: Plot eight points by using concepts of eight-way symmetry.
        _plot_points(x, y)

        x += 1
        if p < 0:
            p = p + 2*x + 1
        else:
            p = p + 2 * x + 1 - 2*y
            y -= 1

    plt.show()


def _plot_points(x, y):
    plt.scatter(x, y, 100, 'black')
    plt.scatter(y, x, 100, 'black')
    plt.scatter(y, -x, 100, 'black')
    plt.scatter(-x, y, 100, 'black')
    plt.scatter(-x, -y, 100, 'black')
    plt.scatter(-y, -x, 100, 'black')
    plt.scatter(-y, x, 100, 'black')
    plt.scatter(x, -y, 100, 'black')

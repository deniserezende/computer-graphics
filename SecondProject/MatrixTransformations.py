import logging
import numpy as np
import matplotlib.pyplot as plt


def _plot_beautify(title: str):
    plt.figure(figsize=(8, 6))
    plt.title(title, fontsize=18, fontweight='bold', color='steelblue', loc='left', pad=15)
    # Add a grid
    plt.grid(True, linestyle='--', linewidth=0.5, color='gray', zorder=-1)

    # Activate a style sheet
    plt.style.use('ggplot')


# DDA
def dda(x_initial, y_initial, x_final, y_final):
    """"The Digital Difference Analyzer (DDA) algorithm is used to draw lines on a screen in an incrementally."""
    logging.getLogger().setLevel(logging.INFO)

    _plot_beautify("Digital Difference Analyzer plot")

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
        plt.scatter(x=round(x), y=round(y), s=30, color='black')
        y = y + y_inc
        x = x + x_inc

    # Set axis limits to show the graph starting at the origin
    if min(x_initial, x_final) >= 0:
        plt.xlim(-0.5, max(x_initial, x_final) + 1)
    if min(y_initial, y_final) >= 0:
        plt.ylim(-0.5, max(y_initial, y_final) + 1)

    # Add axis labels
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')

    plt.show()


# Bresenham's line algorithm
def bresenhams_line_algorithm(x_initial, y_initial, x_final, y_final):
    """"Bresenham's line algorithm is a line drawing algorithm that determines the points of an n-dimensional raster
    that should be selected in order to form a close approximation to a straight line between two points."""
    logging.getLogger().setLevel(logging.INFO)

    _plot_beautify("Bresenham's line plot")

    # Calculate delta
    delta_x = abs(x_final - x_initial)
    delta_y = abs(y_final - y_initial)

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
        _plot_line_first_octant(delta_x, delta_y, x_initial, y_initial, x_final, x_inc, y_inc)
    else:
        _plot_line_second_octant(delta_x, delta_y, x_initial, y_initial, y_final, x_inc, y_inc)

    # Set axis limits to show the graph starting at the origin
    if min(x_initial, x_final) >= 0:
        plt.xlim(-0.5, max(x_initial, x_final) + 1)
    if min(y_initial, y_final) >= 0:
        plt.ylim(-0.5, max(y_initial, y_final) + 1)

    # Add axis labels
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')

    plt.show()


def _plot_line_first_octant(delta_x, delta_y, x_initial, y_initial, x_final, x_inc, y_inc):
    p = 2 * abs(delta_y) - abs(delta_x)
    p2 = 2 * abs(delta_y)
    xy2 = 2 * (abs(delta_y) - abs(delta_x))
    # Plot points
    y = y_initial
    x = x_initial
    plt.scatter(x=round(x), y=round(y), s=30, color='black')

    while x != x_final:
        x += x_inc

        if p < 0:
            p += p2
        else:
            p += xy2
            y += y_inc

        plt.scatter(x=round(x), y=round(y), s=30, color='black')


def _plot_line_second_octant(delta_x, delta_y, x_initial, y_initial, y_final, x_inc, y_inc):
    p = 2 * abs(delta_x) - abs(delta_y)
    p2 = 2 * abs(delta_x)
    xy2 = 2 * (abs(delta_x) - abs(delta_y))

    # Plot points
    y = y_initial
    x = x_initial
    plt.scatter(x=round(x), y=round(y), s=30, color='black')

    while y != y_final:
        y += y_inc

        if p < 0:
            p += p2
        else:
            p += xy2
            x += x_inc

        plt.scatter(x=round(x), y=round(y), s=30, color='black')


# Bresenham's circle algorithm
def bresenhams_circle_algorithm(radius, x_center, y_center):
    """Bresenham's algorithm is used to reduce the calculation needed for drawing a circle by making use of
    property of symmetry.

    Args:
        radius (int): radius of the circle
        x_center (int): x-coordinate of the center of the circle
        y_center (int): y-coordinate of the center of the circle
    """
    logging.getLogger().setLevel(logging.INFO)

    _plot_beautify("Bresenham's circle plot")

    x = 0
    y = radius
    p = 1 - radius
    while x < y:
        _plot_points(x, y, x_center, y_center)

        x += 1
        if p < 0:
            p = p + 2*x + 1
        else:
            p = p + 2 * x + 1 - 2*y
            y -= 1

    plt.show()


def _plot_points(x, y, x_center, y_center):
    plt.scatter(x + x_center, y + y_center, 30, 'black')
    plt.scatter(y + x_center, x + y_center, 30, 'black')
    plt.scatter(y + x_center, -x + y_center, 30, 'black')
    plt.scatter(-x + x_center, y + y_center, 30, 'black')
    plt.scatter(-x + x_center, -y + y_center, 30, 'black')
    plt.scatter(-y + x_center, -x + y_center, 30, 'black')
    plt.scatter(-y + x_center, x + y_center, 30, 'black')
    plt.scatter(x + x_center, -y + y_center, 30, 'black')

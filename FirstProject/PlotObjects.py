import matplotlib.pyplot as plt


def plot_points(points, color):
    # plt.figure()
    for subset in points:
        plt.scatter(x=subset[0], y=subset[1], s=170, color=color)


def finalize_plot():
    plt.show()

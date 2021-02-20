import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np


# method to show maze in the form of an image for easier visualization
def show_maze(maze):
    """
    Method that uses PyPlot to plot the maze on an image to make it easier to see if it was solved and the route to goal
    :param maze: maze to be plotted
    :return: void
    """
    # make color map of fixed colors
    cmap = colors.ListedColormap(['white', 'black', 'tab:red', 'goldenrod'])
    bounds = [0, 1, 2, 3, 4]
    norm = colors.BoundaryNorm(bounds, cmap.N)

    # have imshow show only colors specified on the inputs specified
    plt.imshow(maze, interpolation='none', cmap=cmap, norm=norm)
    plt.grid()
    ax = plt.gca()
    ax.set_yticks(np.arange(-0.5, len(maze), 1))
    ax.set_xticks(np.arange(-0.5, len(maze), 1))
    ax.set_yticklabels([])
    ax.set_xticklabels([])
    plt.show()

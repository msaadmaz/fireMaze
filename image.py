import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np

# method to show maze in the form of an image for easier visualization
def show_maze(maze):
    # make color map of fixed colors
    cmap = colors.ListedColormap(['white', 'black', 'orange', 'grey'])
    bounds = [0, 1, 2, 3, 4]
    norm = colors.BoundaryNorm(bounds, cmap.N)

    # have imshow show only colors specified on the inputs specified
    plt.imshow(maze, interpolation='nearest', cmap=cmap, norm=norm)

    plt.show()


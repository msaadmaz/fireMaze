import numpy as np
from numpy import random

import image
import search

# Checks if neighbors of a given cell are on fire
def neighbor_check(maze, x, y):
    a = 0

    # Checks Top Neighboring cell
    if x - 1 >= 0 and maze[x - 1, y] == 2:
        a += 1

    # Checks Left Neighboring cell
    if y - 1 >= 0 and maze[x, y - 1] == 2:
        a += 1

    # Checks Right Neighboring cell
    if y + 1 < len(maze) and maze[x, y + 1] == 2:
        a += 1

    # Checks the Bottom Cell
    if x + 1 < len(maze) and maze[x + 1, y] == 2:
        a += 1

    return a


# Creates a maze
def create_maze(dim, prob):
    if (prob < 0) or (prob > 1):
        raise Exception("Probability must be 0<p<1")
    arr = np.zeros((dim, dim))
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            r = random.uniform(0, 1)
            if (r < prob) and (x != 0 or y != 0) and (x != dim - 1 or y != dim - 1):
                arr[x, y] = 1
    return arr


# Creates a valid fire maze
def create_fire_maze(dim, prob):
    maze = create_maze(dim, prob)

    # initialize the fire and obtain the coordinates to that fire
    fire_location = start_fire(maze)

    # check to see if there is a path from start to fire, and if not keep checking until there is a valid path
    there_is_path_to_fire = search.dfs(maze, (0, 0), fire_location)
    # set the maze on fire
    maze[fire_location] = 2
    # check to see if the maze is solvable from start to goal, and if not keep checking until there is a valid path
    maze_is_solvable = search.dfs(maze, (0, 0), (dim - 1, dim - 1))
    while not there_is_path_to_fire or not maze_is_solvable:
        maze = create_maze(dim, prob)
        fire_location = start_fire(maze)
        there_is_path_to_fire = search.dfs(maze, (0, 0), fire_location)
        # set the maze on fire
        maze[fire_location] = 2
        maze_is_solvable = search.dfs(maze, (0, 0), (dim - 1, dim - 1))
    # return the maze
    return maze


# Creates a maze with fire increasing every step
def advance_fire_one_step(maze, q):
    copy = maze.copy()
    for x in range(len(copy)):
        for y in range(len(copy[x])):
            if copy[x, y] == 0:
                k = neighbor_check(copy, x, y)
                prob = 1 - ((1 - q) ** k)
                if random.uniform(0, 1) < prob:
                    copy[x, y] = 2
    return copy


def start_fire(maze):
    copy = maze.copy()
    x = random.randint(len(maze))
    y = random.randint(len(maze))
    while copy[x, y] != 0:
        if (x, y) == (0, 0) or (x, y) == (len(maze) - 1, len(maze) - 1):
            continue
        x = random.randint(len(maze))
        y = random.randint(len(maze))

    return x, y

# if __name__ == '__main__':
#     dim = input("Enter Maze Dimensions:")
#     print("Dimensions set to: " + dim)
#     p = input("Enter Probability:")
#     print("Proability is: " + p)
#
#     arr = maze(int(dim), np.double(p))
#     # arr2 = startFire(arr)
# # arr3 = fireMaze(arr2)

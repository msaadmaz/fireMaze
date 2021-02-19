import mazes
import search
import image
from numpy import random


def advance_fire_one_step_strat_3(maze, q):
    copy = maze.copy()
    counter = 0
    for x in range(len(copy)):
        for y in range(len(copy[x])):
            if copy[x, y] == 0:
                k = mazes.neighbor_check(copy, x, y)
                prob = 1 - ((1 - q) ** k)
                i = random.uniform(0, 1)
                if i < prob:
                    copy[x, y] = 2
                    counter += 1
                if i > prob > 0:
                    counter += 1
    if counter == 0:
        return copy, False
    return copy, True


def strat_three(maze, start_state, goal_state, q):
    maze = mazes.start_fire(maze)
    # Test if it

    result = search.dfs(maze, start_state, goal_state)
    if not result:
        return maze, False

    curr = maze
    prev = None
    # Keep checking until maze is no longer solvable
    while result:

        # make a pointer to the current maze
        prev = curr

        # Make the current maze point to the advanced fire maze
        (curr, bool) = advance_fire_one_step_strat_3(curr, q)
        if bool == False:
            return curr, True
        # Run DFS on the new fire maze
        result = search.dfs(curr, start_state, goal_state)
    # Curr Maze is unsolvable while prev maze should be solvable
    (result, count) = search.a_star(prev, start_state, goal_state)
    print(result)
    image.show_maze(curr)
    return prev, result

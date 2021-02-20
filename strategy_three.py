import mazes
import search
import image
from numpy import random


def advance_fire_one_step_strat_3(maze, q):
    """
    Method to advance the fire one step in the maze
    :param maze: maze which will have the fire advanced
    :param q: flammability rate
    :return: a copy of the maze with the fire progressed and a boolean if it was advanced
    """
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
    """
    Method for Strategy three that uses a previous and current maze to test know future outcomes of the maze and get the
    most optimal path using A star before all paths to the goal are set on fire. This is essentially making a game tree
    to understand all future outcomes of the fire and solving before it is unsolvable
    :param maze: The maze we wish to solve
    :param start_state: Initial tile in maze
    :param goal_state: Goal tile in maze
    :param q: Flammability rate
    :return: The final maze and Whether or not the agent was successful
    """
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
        (curr, result2) = advance_fire_one_step_strat_3(curr, q)
        if not result2:
            return curr, True
        # Run DFS on the new fire maze
        result = search.dfs(curr, start_state, goal_state)
    # Curr Maze is unsolvable while prev maze should be solvable
    (result, count, path) = search.a_star(prev, start_state, goal_state)
    # print(result)
    # image.show_maze(prev)
    return prev, result

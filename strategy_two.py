# Strategy two uses BFS to calculate the shortest path to the goal.
# After taking it's first step on that final path the fire is advanced one step, then the BFS algorithm is called again.
# This recall of BFS for each step till the agent makes the goal is to make sure it can avoid the fire as much as
# possible on the way to the goal.
import mazes
import search
from collections import deque


def trace_path_and_advance_fire(maze, path, q, start_state, goal_state):
    for pair in path:
        # tuple unpacking to get coordinates
        (x, y) = pair
        if maze[x, y] == 1:
            raise Exception("You are going through an obstacle")
        if maze[x, y] == 2:
            return maze, False
        # set the path with a 3
        maze[x, y] = 3
        # advance the fire
        maze = mazes.advance_fire_one_step(maze, q)
        if pair == start_state:
            continue
        if pair == goal_state:
            return maze, True
        print(pair)
        # call upon bfs again to make sure we are avoiding the fire as much as possible
        strat_two(maze, pair, (len(maze) - 1, len(maze) - 1), q)

    return maze, True


def strat_two(maze, start_state, goal_state, q):

    # queue fringe of tuples
    fringe = deque()

    # dictionary of tuples that have been checked
    closed_set = set()

    # dictionary of tuples (x,y) coordinates that are the proper path
    prev = {}

    # first item in queue is the start
    fringe.append(start_state)

    while fringe:

        # FIFO
        current_state = fringe.popleft()
        if current_state in closed_set:
            continue
        closed_set.add(current_state)
        if current_state == goal_state:
            # get the path that leads to the goal state
            final_path = search.get_path(prev, start_state, goal_state)
            print(final_path)
            # trace the path in the maze, and call upon BFS every time a step is taken and the fire is advanced
            return trace_path_and_advance_fire(maze, final_path, q, start_state, goal_state)
        # check all the neighbors of current_state and add those to the fringe that are valid
        search.check_neighbors(maze, current_state, fringe, prev, closed_set)

    return maze, False

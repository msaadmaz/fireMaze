# Strategy one calculates the path to the fire without regard to the fire,
# while traversing the shortest path it can still catch on fire as the fire advances each step the agent takes
# towards the goal.
from collections import deque
import mazes
import search


def strategy_one(maze, start_state, goal_state, q):
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
            # trace the path in the maze
            return trace_path_with_fire(maze, final_path, q)
        # check all the neighbors of current_state and add those to the fringe that are valid
        search.check_neighbors(maze, current_state, fringe, prev, closed_set)

    return maze, False


def trace_path_with_fire(maze, path, q):
    for pair in path:
        # tuple unpacking to get coordinates
        (x, y) = pair
        if maze[x, y] == 1:
            raise Exception("You are going through an obstacle")
        if maze[x, y] == 2:
            return maze, False
        # set the path with a 3
        maze[x, y] = 3
        maze = mazes.advance_fire_one_step(maze, q)

    return maze, True

#def test_strat_one
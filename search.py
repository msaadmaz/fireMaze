def check_neighbors(maze, current_state, fringe, prev, closed_set):
    # unpacks tuple
    (x, y) = current_state

    # Checks Top Neighboring cell, and adds to
    if x - 1 >= 0 and maze[x - 1, y] != 1 and (x - 1, y) not in closed_set:
        fringe.append((x - 1, y))
        prev[(x - 1, y)] = current_state
    # Checks right Neighboring cell, and adds to
    if y + 1 < len(maze) and maze[x, y + 1] != 1 and (x, y + 1) not in closed_set:
        fringe.append((x, y + 1))
        prev[(x, y + 1)] = current_state
    # Checks left Neighboring cell, and adds to
    if y - 1 >= 0 and maze[x, y - 1] != 1 and (x, y - 1) not in closed_set:
        fringe.append((x, y - 1))
        prev[(x, y - 1)] = current_state
    # Checks bottom Neighboring cell, and adds to
    if x + 1 < len(maze) and maze[x + 1, y] != 1 and (x + 1, y) not in closed_set:
        fringe.append((x + 1, y))
        prev[((x + 1), y)] = current_state


def dfs(maze, start_state, goal_state):
    # stack fringe of tuples implemented with a list
    fringe = []

    # dictionary of tuples that have been checked
    closed_set = set()

    # dictionary of tuples (x,y) coordinates that are the proper path
    prev = {}

    # first item in stack is the beginning
    fringe.append(start_state)

    while fringe:

        # LIFO stack
        current_state = fringe.pop()
        if current_state == goal_state:
            return True
        # check all the neighbors of current_state and add those to the fringe that are valid
        check_neighbors(maze, current_state, fringe, prev, closed_set)
        closed_set.add(current_state)

    return False


def bfs(maze, start_state, goal_state):
    # queue fringe of tuples implemented with a list
    fringe = []

    # dictionary of tuples that have been checked
    closed_set = set()

    # dictionary of tuples (x,y) coordinates that are the proper path
    prev = {}

    # first item in queue is the start
    fringe.append(start_state)

    while fringe:

        # FIFO list
        current_state = fringe.pop(0)
        if current_state == goal_state:
            final_path = get_path(prev, start_state, goal_state)
            # trace the path in the maze
            trace_path(final_path, maze)
            return True
        # check all the neighbors of current_state and add those to the fringe that are valid
        check_neighbors(maze, current_state, fringe, prev, closed_set)
        closed_set.add(current_state)

    return False


# method to trace prev and get the path that will lead to the goal state
def get_path(prev, start_state, goal_state):
    path = [goal_state]
    while path[-1] != start_state:
        path.append(prev[path[-1]])
    path.reverse()

    # returns a list of tuples that is the path from start to goal
    return path


# method to trace path within the maze
def trace_path(path, maze):

    for pair in path:
        # tuple unpacking to get coordinates
        (x, y) = pair
        if maze[x, y] == 1:
            raise Exception("You are going through an obstacle")
        # set the path with a 3
        maze[x, y] = 3


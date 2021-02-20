from queue import PriorityQueue
import numpy as np
from collections import deque


# method to check the neighbors of a state within the maze
def check_neighbors(maze, current_state, fringe, prev, closed_set):
    # unpacks tuple
    (x, y) = current_state
    count = 0
    # Checks Top Neighboring cell, and adds to fringe if not fire or obstacle
    if x - 1 >= 0 and maze[x - 1, y] != 1 and maze[x - 1, y] != 2:
        if (x - 1, y) not in closed_set:
            fringe.append((x - 1, y))
            count += 1
            prev[(x - 1, y)] = current_state
    # Checks right Neighboring cell, and adds to fringe if not fire or obstacle
    if y + 1 < len(maze) and maze[x, y + 1] != 1 and maze[x, y + 1] != 2:
        if (x, y + 1) not in closed_set:
            fringe.append((x, y + 1))
            count += 1
            prev[(x, y + 1)] = current_state
    # Checks left Neighboring cell, and adds to fringe if not fire or obstacle
    if y - 1 >= 0 and maze[x, y - 1] != 1 and maze[x, y - 1] != 2:
        if (x, y - 1) not in closed_set:
            fringe.append((x, y - 1))
            count += 1
            prev[(x, y - 1)] = current_state
    # Checks bottom Neighboring cell, and adds to fringe if not fire or obstacle
    if x + 1 < len(maze) and maze[x + 1, y] != 1 and maze[x + 1, y] != 2:
        if (x + 1, y) not in closed_set:
            fringe.append((x + 1, y))
            count += 1
            prev[((x + 1), y)] = current_state
    return count


# method to implement DFS, just checks to see if the maze is solvable
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
        if current_state in closed_set:
            continue
        if current_state == goal_state:
            return True
        # check all the neighbors of current_state and add those to the fringe that are valid
        check_neighbors(maze, current_state, fringe, prev, closed_set)
        closed_set.add(current_state)

    return False


# method to implement BFS, checks if the maze is solvable and if it is it will write that path into the maze
def bfs(maze, start_state, goal_state):
    # queue fringe of tuples
    fringe = deque()

    # Count number of nodes explored by BFS
    count = 0

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
            # final_path = get_path(prev, start_state, goal_state)
            # trace the path in the maze
            # trace_path(final_path, maze)
            return True, count
        # check all the neighbors of current_state and add those to the fringe that are valid
        count += check_neighbors(maze, current_state, fringe, prev, closed_set)

    return False, count


# method that implements A* and uses the euclidean distance heuristic to prioritize in the queue. If the maze is
# solvable then it will also write the path into the maze.
def a_star(maze, start_state, goal_state):
    # priority queue fringe of tuples implemented with a list
    fringe = PriorityQueue()

    # Count number of nodes explored by BFS
    count = 0

    # dictionary of tuples that have been checked
    closed_set = set()

    # dictionary of tuples (x,y) coordinates that are the proper path
    prev = {}

    # first item in queue is the start
    fringe.put((0, (0, start_state)))

    while not fringe.empty():

        # priority queue
        (priority, (step, current_state)) = fringe.get()
        if current_state in closed_set:
            continue
        closed_set.add(current_state)
        if current_state == goal_state:
            # get the path that leads to the goal state
            final_path = get_path(prev, start_state, goal_state)
            # trace the path in the maze
            # trace_path(final_path, maze)
            return True, count, final_path
        # check all the neighbors of current_state and add those to the fringe that are valid
        count += check_neighbors_heuristic(maze, current_state, fringe, prev, closed_set, step, goal_state)

    return False, count, []


# method to retrieve euclidean distance
def get_distance(start_state, goal_state):
    # unpack tuples
    (x, y) = start_state
    (i, j) = goal_state
    return np.sqrt((((i - x) ** 2) + ((j - y) ** 2)))


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
            return False
        if maze[x, y] == 2:
            return False
        # set the path with a 3
        maze[x, y] = 3
    return True

# method to check the neighbors of a state within the maze
def check_neighbors_heuristic(maze, current_state, fringe, prev, closed_set, step, goal_state):
    # unpacks tuple
    (x, y) = current_state

    # counts how many neighbors have been explored
    count = 0
    # Checks Top Neighboring cell, and adds to
    if x - 1 >= 0 and maze[x - 1, y] != 1 and maze[x - 1, y] != 2 and (x - 1, y) not in closed_set:
        c_step = step + 1
        total_distance = get_total_distance(c_step, (x - 1, y), goal_state)
        fringe.put((total_distance, (c_step, (x - 1, y))))
        count += 1
        prev[(x - 1, y)] = current_state
    # Checks right Neighboring cell, and adds to
    if y + 1 < len(maze) and maze[x, y + 1] != 1 and maze[x, y + 1] != 2 and (x, y + 1) not in closed_set:
        c_step = step + 1
        total_distance = get_total_distance(c_step, (x, y + 1), goal_state)
        fringe.put((total_distance, (c_step, (x, y + 1))))
        count += 1
        prev[(x, y + 1)] = current_state
    # Checks left Neighboring cell, and adds to
    if y - 1 >= 0 and maze[x, y - 1] != 1 and maze[x, y - 1] != 2 and (x, y - 1) not in closed_set:
        c_step = step + 1
        total_distance = get_total_distance(c_step, (x, y - 1), goal_state)
        fringe.put((total_distance, (c_step, (x, y - 1))))
        count += 1
        prev[(x, y - 1)] = current_state
    # Checks bottom Neighboring cell, and adds to
    if x + 1 < len(maze) and maze[x + 1, y] != 1 and maze[x + 1, y] != 2 and (x + 1, y) not in closed_set:
        c_step = step + 1
        total_distance = get_total_distance(c_step, (x + 1, y), goal_state)
        fringe.put((total_distance, (c_step, (x + 1, y))))
        count += 1
        prev[(x + 1, y)] = current_state
    return count


# gets the total distance from start to current node to goal, this is the priority for the queue
def get_total_distance(step, neighbor, goal_state):
    return step + get_distance(neighbor, goal_state)

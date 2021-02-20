# Strategy two uses BFS to calculate the shortest path to the goal.
# After taking it's first step on that final path the fire is advanced one step, then the BFS algorithm is called again.
# This recall of BFS for each step till the agent makes the goal is to make sure it can avoid the fire as much as
# possible on the way to the goal.
import image
import mazes
import search


def strategy_two(maze, start_state, goal_state, q):
    # initialize a final path to fill into the maze
    final_path = []

    # a pointer to keep track of the state
    current_state = start_state

    while current_state != goal_state:

        # add the current cell into the final path
        final_path.append(current_state)

        # advance the fire one step, as one step was taken in the maze
        maze = mazes.advance_fire_one_step(maze, q)

        (result, nodes_visited, current_path) = search.a_star(maze, current_state, goal_state)

        # the maze is not solvable, the agent ran into the fire
        if not result:
            print("The agent has caught on fire :(")
            return False

        # go to the next tile in the path, increment the pointer
        current_state = current_path[1]

    # the agent has traversed the path
    final_path.append(goal_state)
    search.trace_path(final_path, maze)
    image.show_maze(maze)
    return True

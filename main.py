import image
import mazes
import search
import numpy as np

maze = mazes.maze(100, 0.2)
start_state = (0, 0)
goal_state = (len(maze)-1, len(maze)-1)
result = search.a_star(maze, start_state, goal_state)
if result:
    image.show_maze(maze)
print(result)

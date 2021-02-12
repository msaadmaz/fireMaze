import image
import mazes
import search

maze = mazes.maze(15, 0.3)
start_state = (0, 0)
goal_state = (len(maze)-1, len(maze)-1)
image.show_maze(maze)
result = search.bfs(maze, start_state, goal_state)
if result:
    image.show_maze(maze)


import image
import mazes
import search

maze = mazes.create_maze(100, 0.2)
start_state = (0, 0)
goal_state = (len(maze)-1, len(maze)-1)
result = search.bfs(maze, start_state, goal_state)
if result:
    image.show_maze(maze)
print(result)

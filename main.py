import image
import mazes
import search
import strategy_one

maze = mazes.create_maze(20, 0.3)
start_state = (0, 0)
goal_state = (len(maze)-1, len(maze)-1)
(maze, result) = strategy_one.strat_one(maze, start_state, goal_state, 0.3)
image.show_maze(maze)
print(result)

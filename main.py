import image
import mazes
import search
import strategy_one
import strategy_two

maze = mazes.create_maze(15, 0.3)
maze = mazes.start_fire(maze)
start_state = (0, 0)
goal_state = (len(maze)-1, len(maze)-1)
(maze, result) = strategy_two.strat_two(maze, start_state, goal_state, 0.1)
# (maze, result) = strategy_one.strat_one(maze, start_state, goal_state, 0.3)
image.show_maze(maze)
print(result)

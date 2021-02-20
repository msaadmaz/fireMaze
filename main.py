import time
import mazes
import search
import strategy_one
import strategy_three
import strategy_two
import image
import graphs

# fire_maze = mazes.create_fire_maze(15, 0.3)
# start_state = (0, 0)
# goal_state = (len(fire_maze) - 1, len(fire_maze) - 1)
# strategy_three.strat_three(fire_maze, start_state, goal_state, 0.3)
# strategy_two.strategy_two(fire_maze, start_state, goal_state, 0.3)
# (maze, result) = strategy_one.strategy_one(fire_maze, start_state, goal_state, 0.3)
# print(f'Strategy one result {result}')
# if result:
#     image.show_maze(maze)

# This file was used to test our code
graphs.test_fire_maze_strategies(20)

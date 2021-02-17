import numpy as np
def test(s, g):
    x = 0.1
    prob_counter=0
    xpoints = np.array([])
    while x<1:
        for i in range(10):
            maze = mazes.maze(10, x)
            result = search.dfs(maze, s, g)
            if result:
                prob_counter+=1
        prob_counter = prob_counter / 10
        xpoints = np.append(xpoints, [prob_counter])
        prob_counter = 0
        x+=0.1
    ypoints = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
    print(xpoints)
    plt.plot(xpoints, ypoints)
    plt.show()

maze = mazes.maze(10, 0.2)
start_state = (0, 0)
goal_state = (len(maze)-1, len(maze)-1)
result = search.a_star(maze, start_state, goal_state)
if result:
    image.show_maze(maze)
test(start_state, goal_state)
print(result)

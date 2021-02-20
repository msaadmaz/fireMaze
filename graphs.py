import strategy_one
import strategy_two
import strategy_three
import numpy as np
import matplotlib.pyplot as plt
import mazes
import search


def test_dfs(dim):
    x = 0.1
    prob_counter = 0
    xpoints = np.array([])
    while x < 1:
        for i in range(50):
            maze = mazes.create_maze(dim, x)
            s = (0, 0)
            g = (len(maze) - 1, len(maze) - 1)
            result = search.dfs(maze, s, g)
            if result:
                prob_counter += 1
            #
            # image.show_maze(maze)
        prob_counter = prob_counter / 50
        xpoints = np.append(xpoints, [prob_counter])
        prob_counter = 0
        x += 0.1
    ypoints = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
    print(xpoints)
    plt.plot(xpoints, ypoints)
    plt.xlabel("Probability that S can be reached from G")
    plt.ylabel("Obstacle Density p")
    plt.show()


def test_bfs_a_star(dim):
    x = 0.1
    bfs_counter = 0
    a_star_counter = 0
    ypoints = np.array([])
    y1points = np.array([])
    while x < 1:
        for i in range(50):
            maze = mazes.create_maze(dim, x)
            s = (0, 0)
            g = (len(maze) - 1, len(maze) - 1)
            result = search.bfs(maze, s, g)
            result2 = search.a_star(maze, s, g)
            bfs_counter += result[1]
            a_star_counter += result2[1]

        bfs_counter = bfs_counter / 50
        a_star_counter = a_star_counter / 50
        difference = bfs_counter - a_star_counter
        ypoints = np.append(ypoints, [difference])
        bfs_counter = 0
        a_star_counter = 0
        x += 0.1
    xpoints = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
    print(ypoints)
    plt.plot(xpoints, ypoints)
    plt.ylabel("Difference between 'Nodes explored by BFS and A*' ")
    plt.xlabel("Obstacle Density p")
    plt.show()


def test_fire_maze_strategies(dim):
    x = 0.1
    c1 = 0
    c2 = 0
    c3 = 0
    x1 = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
    x2 = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
    x3 = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
    y1 = np.array([])
    y2 = np.array([])
    y3 = np.array([])
    while x < 1:
        for i in range(50):
            maze = mazes.create_maze(dim, 0.3)
            s = (0, 0)
            g = (len(maze) - 1, len(maze) - 1)
            if strategy_one.strat_one(maze, s, g, x)[1]:
                c1 += 1
            #if strategy_two.strat_two(maze, s, g, x)[1]:
            #    c2 += 1
            if strategy_three.strat_three(maze, s, g, x)[1]:
                c3 += 1
        c1 = c1 / 50
        y1 = np.append(y1, [c1])
        #c2 = c2 / 50
        #y2 = np.append(y2, [c2])
        c3 = c3 / 50
        y3 = np.append(y3, [c3])
        x += 0.1

    plt.plot(x1, y1, label = "strat 1")
   # plt.plot(x2, y2, label = "strat 2")
    plt.plot(x3, y3, label = "strat 3")
    plt.ylabel("Average Success ")
    plt.xlabel("Flammability q")
    plt.legend()
    plt.title("Strategy 1 vs Strategy 2 vs FFFF")
    plt.show()

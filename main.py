import time
import numpy as np
import mazes
import search
import image
import matplotlib.pyplot as plt
#def strat_3:


def test_dfs(dim):
    x = 0.1
    prob_counter=0
    xpoints = np.array([])
    while x<1:
        for i in range(50):
            maze = mazes.maze(dim, x)
            s= (0, 0)
            g = (len(maze) - 1, len(maze) - 1)
            result = search.dfs(maze, s, g)
            if result:
                prob_counter+=1
            #
                #image.show_maze(maze)
        prob_counter = prob_counter / 50
        xpoints = np.append(xpoints, [prob_counter])
        prob_counter = 0
        x+=0.1
    ypoints = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
    print(xpoints)
    plt.plot(xpoints, ypoints)
    plt.xlabel("Probability that S can be reached from G")
    plt.ylabel("Obstacle Density p")
    plt.show()

def test_bfs_a_star(dim):
    x = 0.1
    bfs_counter=0
    a_star_counter =0
    ypoints = np.array([])
    y1points = np.array([])
    while x<1:
        for i in range(50):
            maze = mazes.maze(dim, x)
            s= (0, 0)
            g = (len(maze) - 1, len(maze) - 1)
            result = search.bfs(maze, s, g)
            result2 = search.a_star(maze, s, g)
            bfs_counter += result[1]
            a_star_counter += result2[1]

        bfs_counter = bfs_counter / 50
        a_star_counter = a_star_counter / 50
        difference = bfs_counter-a_star_counter
        ypoints = np.append(ypoints, [difference])
        bfs_counter = 0
        a_star_counter = 0
        x+=0.1
    xpoints = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
    print(ypoints)
    plt.plot(xpoints, ypoints)
    plt.ylabel("Difference between 'Nodes explored by BFS and A*' ")
    plt.xlabel("Obstacle Density p")
    plt.show()

if __name__ == '__main__':
    # starting time
    start = time.time()

    # program body ends

    test_dfs()
    test_bfs_a_star()

   # maze = mazes.maze(4100, 0.3) # Maximum dimension size for Hassaan is 3,923,339
    #start_state = (0, 0)
   # goal_state = (len(maze)-1, len(maze)-1)
    #result = search.bfs(maze, start_state, goal_state)
    #if result:
   #    image.show_maze(maze)
    #print(result)




    # end time
    end = time.time()
    # total time taken
    print(f"Runtime of the program is {end - start}")
    #maze = mazes.maze(10, 0.1) # Maximum dimension size for Hassaan is 3,923,339
    #start_state = (0, 0)
   # goal_state = (len(maze)-1, len(maze)-1)
   # result = search.a_star(maze, start_state, goal_state)
   # if result:
   #     image.show_maze(maze)
    #print(result)

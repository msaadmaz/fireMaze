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

    # Checks Lower Neighboring cell
        if arr[x + 1, y] != None and arr[x - 1, y] == 2:
            a+=1

    # Checks Lower Right Neighboring cell
        if arr[x + 1, y + 1] != None and arr[x + 1, y + 1] == 2:
            a+=1
    return a
#Creates a maze
def maze(dim, prob):
    if (prob < 0) or (prob > 1):
        raise Exception("Probability must be 0<p<1")
    arr = np.zeros((dim,dim))
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            r = random.uniform(0,1)
            if (r< prob) and (x!=0 and y!=0) and (x!=dim-1 and y!= dim-1):
                    arr[x,y] = 1
    print(arr)
    return arr
# Creates a maze with fire increasing every step
def fireMaze (arr):
    fire = arr.copy()
    for x in range(len(fire)):
        for y in range(len(fire[x])):
            if fire[x,y] ==0:
                k = neighborcheck(fire, x, y)
                prob = 1 - pow((1-0.5), k)
                if random.uniform(0,1) < prob:
                    fire[x,y]=2
    print("FireMaze")
    print(fire)
    return fire

def startFire(arr):
    arr2 = arr.copy()
    x = random.randint(4)
    y = random.randint(4)
    while(arr2[x,y] !=0):
        x = random.randint(4)
        y = random.randint(4)
    arr2[x,y] = 2
    print(arr2)
    return arr2

if __name__ == '__main__':
    dim = input("Enter Maze Dimensions:")
    print("Dimensions set to: " + dim)
    p = input("Enter Probability:")
    print("Proability is: " + p)

    arr = maze(int(dim), np.double(p))
    #arr2 = startFire(arr)
   # arr3 = fireMaze(arr2)

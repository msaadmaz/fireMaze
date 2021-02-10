import numpy as np
from numpy import random
#Checks if neighbors of a given cell are on fire
def neighborcheck (arr, x, y):
    a=0
    # Checks Upper Left Neighboring cell
    if arr[x-1,y-1]!= None and arr[x-1,y-1]==2:
        a+=1

    # Checks Top Neighboring cell
    if arr[x - 1, y] != None and arr[x - 1, y] == 2:
        a+=1

    # Checks Upper Right Neighboring cell
    if (y+1) != 5:
        if arr[x - 1, y + 1] != None and arr[x - 1, y + 1] == 2:
            a+=1

    # Checks Left Neighboring cell
    if arr[x, y - 1] != None and arr[x, y - 1] == 2:
        a+=1

    # Checks Right Neighboring cell
    if (y + 1) != 5:
        if arr[x, y + 1] != None and arr[x, y + 1] == 2:
            a+=1

    # Checks Lower Left Neighboring cell
    if (x + 1) != 5 and (y+1)!=5:
        if arr[x + 1, y - 1] != None and arr[x + 1, y - 1] == 2:
            a+=1

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

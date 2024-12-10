import time
import numpy as np

D10I = open("/Users/nicholas/Desktop/Advent of Code 2024/Day10/Day10Input.txt", "r").read()

start_time = time.time()

preGrid = D10I.splitlines()

for line in range(len(preGrid)):
    preGrid[line] = list(preGrid[line])
    for char in range(len(preGrid[line])):
        preGrid[line][char] = int(preGrid[line][char])

grid = np.array(preGrid)

trailhead_coords = list(zip(*np.where(grid == 0)))


def finishPath(currPos, num):
    global trailhead_rating
    global peaks_reached
    if (num != 9):
        #UP
        if currPos[0] > 0:
            if(grid[currPos[0]-1, currPos[1]] == num+1):
                finishPath((currPos[0]-1, currPos[1]), num + 1)
        #DOWN
        if currPos[0] < grid.shape[0]-1:
            if(grid[currPos[0]+1, currPos[1]] == num+1):
                finishPath((currPos[0]+1, currPos[1]), num + 1)
        #LEFT
        if currPos[1] > 0:
            if(grid[currPos[0], currPos[1]-1] == num+1):
                finishPath((currPos[0], currPos[1]-1), num + 1)
        #RIGHT
        if currPos[1] < grid.shape[1]-1:
            if(grid[currPos[0], currPos[1]+1] == num+1):
                finishPath((currPos[0], currPos[1]+1), num + 1)
    else:
        trailhead_rating += 1
        if (not currPos in peaks_reached):
            peaks_reached.append(currPos)

trailhead_score_sum = 0
trailhead_rating_sum = 0
for trailhead in trailhead_coords:
    trailhead_rating = 0
    peaks_reached = []
    finishPath(trailhead, 0)
    trailhead_score_sum += len(peaks_reached)
    trailhead_rating_sum += trailhead_rating

print(trailhead_score_sum)
print(trailhead_rating_sum)




print(str(time.time()-start_time) + " seconds")
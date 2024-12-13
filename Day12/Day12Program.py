import time
import numpy as np

D12I = open("/Users/nicholas/Desktop/Advent of Code 2024/Day12/Day12Input.txt", "r").read()

start_time = time.time()

preGrid = D12I.splitlines()

for line in range(len(preGrid)):
    preGrid[line] = list(preGrid[line])

grid = np.array(preGrid)


def findPerimeter(region, cropType):
    perimeter = []
    for crop in region:
        #UP
        if crop[0] > 0:
            if(grid[crop[0]-1, crop[1]] != cropType):
                perimeter.append((crop[0]-1, crop[1]))

        else:
            perimeter.append((crop[0]-1, crop[1]))
        #DOWN
        if crop[0] < grid.shape[0]-1:
            if(grid[crop[0]+1, crop[1]] != cropType):
                perimeter.append((crop[0]+1, crop[1]))
        else:
            perimeter.append((crop[0]+1, crop[1]))
        #LEFT
        if crop[1] > 0:
            if(grid[crop[0], crop[1]-1] != cropType):
                perimeter.append((crop[0], crop[1]-1))
        else:
            perimeter.append((crop[0], crop[1]-1))
        #RIGHT
        if crop[1] < grid.shape[1]-1:
            if(grid[crop[0], crop[1]+1] != cropType):
                perimeter.append((crop[0], crop[1]+1))
        else:
            perimeter.append((crop[0], crop[1]+1))
    return perimeter

def findNeighbors(pos):
    return[
        (pos[0] - 1, pos[1]),    # UP
        (pos[0] - 1, pos[1]+1),  # UPRIGHT
        (pos[0], pos[1] + 1),    # RIGHT
        (pos[0]+1, pos[1] + 1),  # DOWNRIGHT
        (pos[0] + 1, pos[1]),    # DOWN
        (pos[0]+1, pos[1]-1),    # DOWNLEFT
        (pos[0], pos[1] - 1),    # LEFT
        (pos[0]-1, pos[1] - 1)   # UPLEFT
    ]
    

def findSides(region):
    sides = 0
    regionMap = np.zeros(grid.shape, int)
    for point in region:
        regionMap[point] = 1
    print(regionMap)
    for point in region:
        neighbors = findNeighbors(point)
        # Outside Corners
        if (neighbors[0] not in region and neighbors[1] not in region and neighbors[2] not in region):
            point = "X"
            sides += 1
        if (neighbors[2] not in region and neighbors[3] not in region and neighbors[4] not in region):
            point = "X"
            sides += 1
        if (neighbors[4] not in region and neighbors[5] not in region and neighbors[6] not in region):
            point = "X"
            sides += 1
        if (neighbors[6] not in region and neighbors[7] not in region and neighbors[0] not in region):
            point = "X"
            sides += 1
        
        # Inside Corners
        if (neighbors[1] in region and neighbors[0] not in region):
            point = "X"
            sides += 1
        if (neighbors[7] in region and neighbors[0] not in region):
            point = "X"
            sides += 1
        if (neighbors[3] in region and neighbors[4] not in region):
            point = "X"
            sides += 1
        if (neighbors[5] in region and neighbors[4] not in region):
            point = "X"
            sides += 1
    
    return sides

def finishRegion(currPos, char):
    global visitedSpaces
    global region
    visitedSpaces.append(currPos)
    region.append(currPos)
    #UP
    if currPos[0] > 0:
        if(grid[currPos[0]-1, currPos[1]] == char and not ((currPos[0]-1, currPos[1]) in visitedSpaces)):
            finishRegion((currPos[0]-1, currPos[1]), char)
    #DOWN
    if currPos[0] < grid.shape[0]-1:
        if(grid[currPos[0]+1, currPos[1]] == char and not (currPos[0]+1, currPos[1]) in visitedSpaces):
            finishRegion((currPos[0]+1, currPos[1]), char)
    #LEFT
    if currPos[1] > 0:
        if(grid[currPos[0], currPos[1]-1] == char and not (currPos[0], currPos[1]-1) in visitedSpaces):
            finishRegion((currPos[0], currPos[1]-1), char)
    #RIGHT
    if currPos[1] < grid.shape[1]-1:
        if(grid[currPos[0], currPos[1]+1] == char and not (currPos[0], currPos[1]+1) in visitedSpaces):
            finishRegion((currPos[0], currPos[1]+1), char)

visitedSpaces = []
regions = []
for row in range(len(grid)):
    for crop in range(len(grid[row])):
        if not (row, crop) in visitedSpaces:
            region = []
            finishRegion((row, crop), grid[row, crop])
            regions.append((region, grid[row, crop]))


def partOne():
    price = 0
    for region in regions:
        area = len(region[0])
        perim = len(findPerimeter(region[0], region[1]))
        price += area*perim
        print(f'Area: {area}, Perimeter: {perim}, Price: {area*perim}')

    print(f'Total Price: {price}')

def partTwo():
    price = 0
    c = 0
    for region in regions:
        area = len(region[0])
        sides = findSides(region[0])
        price += area*sides
        c += 1
        print(f'Region: {c}/{len(regions)} \n Area: {area}, Sides: {sides}, Price: {area*sides}')

    print(f'Total Price: {price}')

partOne()
partTwo()


print(str(time.time()-start_time) + " seconds")
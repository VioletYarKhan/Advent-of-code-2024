from itertools import product
import time

D8I = open("/Users/nicholas/Desktop/Advent of Code 2024/Day8/Day8Input.txt", "r")

start_time = time.time()
grid = []

for line in D8I:
    grid.append(line.strip())


def in_bounds(r, c):
    if(0 <= r < len(grid) and 0 <= c < len(grid[0])):
        return True
    return False

def remove_and_insert(string, index, new_string):
  return string[:index] + new_string + string[index + 1:]

frequencies = []

for line in grid:
    for char in line:
        if(char != "." and not (char in frequencies)):
            frequencies.append(char)
def partOne():
    antinode_count = 0
    p1Grid = grid.copy()
    for freq in frequencies:
        countingGrid = grid.copy()
        freqCoords = []
        for y in range(len(countingGrid)):
            for x, char in enumerate(countingGrid[y]):
                if char == freq:
                    freqCoords.append((y, x))
        
        for coord in freqCoords:
            for compCoord in freqCoords:
                if (coord != compCoord):
                    diff = (compCoord[0]-coord[0], compCoord[1]-coord[1])
                    new_antinode = (compCoord[0]+diff[0], compCoord[1]+diff[1])
                    if(in_bounds(new_antinode[0], new_antinode[1])):
                        countingGrid[new_antinode[0]] = remove_and_insert(countingGrid[new_antinode[0]], new_antinode[1], "#")
                        p1Grid[new_antinode[0]] = remove_and_insert(p1Grid[new_antinode[0]], new_antinode[1], "#")
    for row in p1Grid:
        print(row)
        for element in row:
            if (element == "#"):
                antinode_count += 1
    print(antinode_count)    

def partTwo():
    antinode_count = 0
    p2Grid = grid.copy()
    for freq in frequencies:
        countingGrid = grid.copy()
        freqCoords = []
        for y in range(len(countingGrid)):
            for x, char in enumerate(countingGrid[y]):
                if char == freq:
                    freqCoords.append((y, x))
        
        for coord in freqCoords:
            for compCoord in freqCoords:
                if (coord != compCoord):
                    diff = (compCoord[0]-coord[0], compCoord[1]-coord[1])
                    new_antinode = coord[0], coord[1]
                    while(in_bounds(new_antinode[0], new_antinode[1])):
                        countingGrid[new_antinode[0]] = remove_and_insert(countingGrid[new_antinode[0]], new_antinode[1], "#")
                        p2Grid[new_antinode[0]] = remove_and_insert(p2Grid[new_antinode[0]], new_antinode[1], "#")
                        new_antinode = (new_antinode[0]+diff[0], new_antinode[1]+diff[1])
    for row in p2Grid:
        print(row)
        for element in row:
            if (element == "#"):
                antinode_count += 1
    print(antinode_count)    

partOne()
partTwo()


print(str(time.time()-start_time) + " seconds")
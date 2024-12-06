import regex as re
import time
D6I = open("/Users/nicholas/Desktop/Advent of Code 2024/Day6/Day6Input.txt", "r")

grid = []
for line in D6I:
    grid.append(line.strip())

start_time = time.time()

def in_bounds(r, c):
    if(0 <= r < len(grid) and 0 <= c < len(grid[0])):
        return True
    return False

def remove_and_insert(string, index, new_string):
  return string[:index] + new_string + string[index + 1:]

for i in range(len(grid)):
    if("^" in grid[i]):
        startingPosition = [i, grid[i].index("^")]

direction = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1)
]

def partOne():
    visitedCount = 0
    dr = 0
    inputGrid = grid.copy()
    player_position = startingPosition.copy()

    while True:
        if (in_bounds(player_position[0] + direction[dr][0], player_position[1] + direction[dr][1])):
            next_position = [player_position[0] + direction[dr][0], player_position[1] + direction[dr][1]]
            if(inputGrid[next_position[0]][next_position[1]] != "#"):
                inputGrid[player_position[0]] = remove_and_insert(inputGrid[player_position[0]], player_position[1], "X")
                player_position = next_position
            elif(inputGrid[next_position[0]][next_position[1]] == "#"):
                if (dr < 3):
                    dr += 1
                else:
                    dr = 0
        else:
            inputGrid[player_position[0]] = remove_and_insert(inputGrid[player_position[0]], player_position[1], "X")
            for row in inputGrid:
                print(row)
                for element in row:
                    if (element == "X"):
                        visitedCount += 1
            break
    print(visitedCount)
    return "Finished"


visitedCount = 0

def pathWillEnd(inputGrid, currPos):
    dr = 0
    visitedPositions = [(currPos, dr)]
    while True:
        if (in_bounds(currPos[0] + direction[dr][0], currPos[1] + direction[dr][1])):
            next_position = [currPos[0] + direction[dr][0], currPos[1] + direction[dr][1]]
            if((next_position, dr) in visitedPositions):
                return False, visitedPositions
            if(inputGrid[next_position[0]][next_position[1]] != "#"):
                visitedPositions.append((currPos, dr))
                currPos = next_position
            elif(inputGrid[next_position[0]][next_position[1]] == "#"):
                if (dr < 3):
                    dr += 1
                else:
                    dr = 0
        else:
            visitedPositions.append((next_position, dr))
            return True, visitedPositions

def partTwo():
    row_start_time = time.time()
    loops = 0
    print(f"Columns per row: {len(grid[0])}")
    basicPath = []
    for position in pathWillEnd(grid.copy(), startingPosition)[1]:
        basicPath.append(position[0])
    for row in range(len(grid)):
        row_start_time = time.time()
        for col in range(len(grid[0])):
            if (grid[row][col] != "^") and ([row, col] in basicPath):
                currGrid = grid.copy()
                currGrid[row] = remove_and_insert(currGrid[row], col, "#")
                if(not pathWillEnd(currGrid.copy(), startingPosition)[0]):
                    loops += 1
        print(f"Row: {row}/{130} \n Time: {time.time()-row_start_time} \n Total Time: {time.time()-start_time}")
    print(loops)

partOne()
partTwo()
print(str(time.time()-start_time) + " seconds")
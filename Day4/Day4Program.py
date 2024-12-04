import regex as re

D4I = open("/Users/nicholas/Desktop/Advent of Code 2024/Day4/Day4Input.txt", "r")

grid = []
for line in D4I.readlines():
    grid.append(line.strip())


rows = len(grid)
cols = len(grid[0])

def in_bounds(r, c):
    if(0 <= r < rows and 0 <= c < cols):
        return True
    return False

word = "XMAS"

directions = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
    (1, 1),
    (-1, -1),
    (1, -1),
    (-1, 1)
]
def partOne():
    total_count = 0
    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                correct_letters = 0
                for i in range(len(word)):
                    if (
                        in_bounds(r + dr * i, c + dc * i) and
                        grid[r + dr * i][c + dc * i] == word[i]
                    ): 
                        correct_letters += 1
                if(correct_letters == 4):
                    total_count += 1
    print(total_count)

def partTwo():
    total_count = 0
    mas_sequences = []
    for r in range(rows):
        for c in range(cols):
            if in_bounds(r + 2, c + 2):
                if grid[r][c] == 'M' and grid[r + 1][c + 1] == 'A' and grid[r + 2][c + 2] == 'S':
                    mas_sequences.append(((r, c), (r + 1, c + 1), (r + 2, c + 2)))
            if in_bounds(r + 2, c - 2):
                if grid[r][c] == 'M' and grid[r + 1][c - 1] == 'A' and grid[r + 2][c - 2] == 'S':
                    mas_sequences.append(((r, c), (r + 1, c - 1), (r + 2, c - 2)))
            if in_bounds(r - 2, c - 2):
                if grid[r][c] == 'M' and grid[r - 1][c - 1] == 'A' and grid[r - 2][c - 2] == 'S':
                    mas_sequences.append(((r, c), (r - 1, c - 1), (r - 2, c - 2)))
            if in_bounds(r - 2, c + 2):
                if grid[r][c] == 'M' and grid[r - 1][c + 1] == 'A' and grid[r - 2][c + 2] == 'S':
                    mas_sequences.append(((r, c), (r - 1, c + 1), (r - 2, c + 2)))
    for i in range(len(mas_sequences)):
        for j in range(i+1, len(mas_sequences)):
            if(mas_sequences[i][1]==mas_sequences[j][1]):
                total_count += 1
                break
    print(total_count)

partOne()
partTwo()
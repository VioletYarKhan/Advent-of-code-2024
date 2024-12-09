from itertools import product
import time

D9I = open("/Users/nicholas/Desktop/Advent of Code 2024/Day9/Day9Input.txt", "r").read()

start_time = time.time()

files = []


for id in range(len(D9I)):
    if(id%2 == 0):
        files.append([int(D9I[id])])
    else:
        files[-1].append(int(D9I[id]))

disk_map = []
for id in range(len(files)):
    file = files[id]
    for used_storage in range(file[0]):
        disk_map.append(str(id))
    if (len(file) > 1):
        for unused_storage in range(file[1]):
            disk_map.append(".")

def partOne():
    for moving_id in range(1, len(disk_map) - 1):
        if not "." in disk_map[:-moving_id]:
            break
        char = disk_map[-moving_id]
        if char != ".":
            moveTo = disk_map.index(".")
            disk_map[moveTo] = char
            disk_map[-moving_id] = "."

    total = 0
    for checksum_pos in range(len(disk_map)):
        checksum_val = disk_map[checksum_pos]
        if checksum_val != ".":
            total += int(checksum_val)*checksum_pos
        else:
            break

    print(total)


def findEmptySpace(n, lst):
    for i in range(len(lst) - n + 1):
        if lst[i:i + n] == ['.'] * n:
            return i
    return -1
def partTwo():
    moving_id = 1
    while moving_id < len(disk_map):
        if not "." in disk_map[:-moving_id]:
            break
        char = disk_map[-moving_id]
        if char != ".":
            lengthOfUsed = 1
            while (disk_map[-(moving_id+1)] == char):
                lengthOfUsed += 1
                moving_id += 1
            
            moveTo = findEmptySpace(lengthOfUsed, disk_map)
            if (moveTo < len(disk_map)-moving_id and moveTo != -1):
                for i in range(moveTo, moveTo+lengthOfUsed):
                    disk_map[i] = char
                    for j in range(lengthOfUsed):
                        disk_map[-(moving_id)+j] = "."
        moving_id += 1

    total = 0
    for checksum_pos in range(len(disk_map)):
        checksum_val = disk_map[checksum_pos]
        if checksum_val != ".":
            total += int(checksum_val)*checksum_pos

    print(total)


partOne()
partTwo()

print(str(time.time()-start_time) + " seconds")
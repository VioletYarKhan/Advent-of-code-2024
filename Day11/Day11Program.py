import time
from collections import Counter

D10I = open("/Users/nicholas/Desktop/Advent of Code 2024/Day11/Day11Input.txt", "r").read()

start_time = time.time()


def count_stones_after_blinks(initial_stones, blinks):
    stone_counts = Counter(initial_stones)
    
    for i in range(blinks):
        blink_start_time = time.time()
        new_counts = Counter()
        
        for stone, count in stone_counts.items():
            if stone == 0:
                new_counts[1] += count
            elif len(str(stone)) % 2 == 0:
                stone_str = str(stone)
                mid = len(stone_str) // 2
                left = int(stone_str[:mid])
                right = int(stone_str[mid:])
                new_counts[left] += count
                new_counts[right] += count
            else:
                new_counts[stone * 2024] += count
        
        stone_counts = new_counts
        print(f"Blink: {i}/{blinks} \n Time: {time.time()-blink_start_time} \n Total Time: {time.time()-start_time}")

    return sum(stone_counts.values())

initial_stones = D10I.split(" ")
for s in range(len(initial_stones)):
    initial_stones[s] = int(initial_stones[s])
blinks = 25
result = count_stones_after_blinks(initial_stones, blinks)
print(f"Number of stones after {blinks} blinks: {result}")

blinks = 75
result = count_stones_after_blinks(initial_stones, blinks)
print(f"Number of stones after {blinks} blinks: {result}")



print(str(time.time()-start_time) + " seconds")
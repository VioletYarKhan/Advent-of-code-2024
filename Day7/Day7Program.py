from itertools import product
import time
from operator import add, mul
D6I = open("/Users/nicholas/Desktop/Advent of Code 2024/Day7/Day7Input.txt", "r")

start_time = time.time()
test_val = []
numbers = []
for line in D6I:
    next_line = line.split(":")
    test_val.append(int(next_line[0]))
    numbers.append(list(map(int, next_line[1].strip().split())))

def partOne():
    calibration_result = 0
    for i in range(len(test_val)):
        num_operators = len(numbers[i]) - 1
        possibilities = list(product("*+", repeat=num_operators))
        for j in range(len(possibilities)):
            total = numbers[i][0]
            for k in range(len(possibilities[j])):
                if(possibilities[j][k] == "+"):
                    total += numbers[i][k+1]
                else:
                    total *= numbers[i][k+1]
                if (total > test_val[i]):
                    break
            if (total == test_val[i]):
                calibration_result += total
                break

    print(calibration_result)

def partTwo():
    calibration_result = 0
    for i in range(len(test_val)):
        num_operators = len(numbers[i]) - 1
        possibilities = list(product("+*|", repeat=num_operators))
        for j in range(len(possibilities)):
            total = numbers[i][0]
            for k in range(len(possibilities[j])):
                if(possibilities[j][k] == "+"):
                    total += numbers[i][k+1]
                elif(possibilities[j][k] == "*"):
                    total *= numbers[i][k+1]
                else:
                    total = int(str(total) + str(numbers[i][k + 1]))
                if (total > test_val[i]):
                    break
            if (total == test_val[i]):
                calibration_result += total
                break

    print(calibration_result)


print(str(time.time()-start_time) + " seconds")
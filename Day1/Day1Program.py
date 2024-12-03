

file = open("/Users/nicholas/Desktop/Advent of Code 2024/Day1/Day1Input.txt", "r")
print("START")
L1 = []
L2 = []

LinesList = (line.split() for line in file)

for line in LinesList:
    L1.append(line[0])
    L2.append(line[1])

L1.sort()
L2.sort()

def partOne():
    distanceSum = 0
    for i in range(len(L1)):
        distanceSum += abs(int(L1[i])-int(L2[i]))
    print(distanceSum)

def partTwo():
    similarityScore = 0
    for i in range(len(L1)):
        similarityScore += int(L1[i])*L2.count(L1[i])
    print(similarityScore)

# partOne()
# partTwo()
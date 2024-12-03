file = open("/Users/nicholas/Desktop/Advent of Code 2024/Day2/Day2Input.txt", "r")
sampleFile = open("/Users/nicholas/Desktop/Advent of Code 2024/Day2/Day2Sample.txt", "r")


print("START")

realLines = (line.split() for line in file)
sampleLines = (line.split() for line in sampleFile)

def isSafe(line):
    for i in range(len(line)):
        line[i] = int(line[i]) 
    sortedLine = sorted(line)
    reverseSortedLine = sorted(line)[::-1]

    if (line != sortedLine and line != reverseSortedLine):
        return False
    for i in range(len(line)-1):
        if(not(1 <= (abs(int(line[i])-int(line[i+1]))) <= 3)):
            return False
    return True

def part1(lines):
    safeReports = 0
    for line in lines:
        if(isSafe(line)):
            safeReports += 1
            
    print(safeReports)

def part2(lines):
    safeReports = 0
    for line in lines:
        if(isSafe(line)):
            safeReports += 1
        else:
            for i in range(len(line)):
                usedline = []
                for j in range(len(line)):
                    usedline.append(line[j])
                del usedline[i]
                if(isSafe(usedline)):
                    safeReports += 1
                    break
            
    print(safeReports)

part1(realLines)
#part2(realLines)
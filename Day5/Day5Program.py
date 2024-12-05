import regex as re

D5I = open("/Users/nicholas/Desktop/Advent of Code 2024/Day5/Day5Input.txt", "r")

rules = []
updates = []

updateRead = False
for line in D5I.readlines():
    if(line == "\n"):
        updateRead = True
    else:
        if(not updateRead):
            rules.append(line.strip().split("|"))
        else:
            updates.append(line.strip().split(","))


def isValid(page1, page2):
    if [page1, page2] in rules:
        return True
    return False

orderedUpdates = []
unOrderedUpdates = []
for update in updates:
    updateIsOrdered = True
    for i in range(len(update)-1):
        if(not isValid(update[i], update[i+1])):
            updateIsOrdered = False
    if(updateIsOrdered):
        orderedUpdates.append(update)
    else:
        unOrderedUpdates.append(update)


def partOne():
    sum = 0
    for update in orderedUpdates:
        sum += int(update[int((len(update)-1)/2)])

    print(sum)
def partTwo():
    for update in unOrderedUpdates:
        for i in range(len(update)-1):
            if(not isValid(update[i], update[i+1])):
                for k in range(len(update) - 1):
                    for l in range(k + 1, len(update)):
                        if not isValid(update[k], update[l]):
                            update[k], update[l] = update[l], update[k]
    sum = 0
    for update in unOrderedUpdates:
        sum += int(update[int((len(update)-1)/2)])

    print(sum)

partOne()
partTwo()
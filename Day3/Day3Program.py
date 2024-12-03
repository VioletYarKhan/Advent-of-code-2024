import regex as re

D3I = open("/Users/nicholas/Desktop/Advent of Code 2024/Day3/Day3Input.txt", "r")
memory = D3I.read()
# memory = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

mul_pattern = re.compile("mul\(\d{1,3},\d{1,3}\)")
instruction_pattern = re.compile("(mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\))")

mul_instructions = re.findall(mul_pattern, memory)
instructions = re.findall(instruction_pattern, memory)

def partOne():
    result = 0
    for instr in mul_instructions:
        numbers = re.findall(r"\d{1,3}", instr)
        x = int(numbers[0])
        y = int(numbers[1])
        result += x * y
    print(result)

def partTwo():
    mul_enabled = True
    result = 0
    for instr in instructions:
        if instr == "do()":
            mul_enabled = True
        elif instr == "don't()":
            mul_enabled = False
        elif ("mul" in instr) and (mul_enabled):
            numbers = re.findall("\d{1,3}", instr)
            x = int(numbers[0])
            y = int(numbers[1])
            result += x * y

    print(result)

partOne()
partTwo()
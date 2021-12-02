horizontal = 0
depth = 0
aim = 0

with open('input.txt', 'r') as file:
    lines = file.readlines()
    instructions = (line.strip('\n') for line in lines)
    for instruction in instructions:
        command, value = instruction.split(' ')
        value = int(value)

        if command == 'forward':
            horizontal += value
            depth += aim * value
        elif command == 'up':
            aim -= value
        elif command == 'down':
            aim += value
        else:
            print('Invalid command', command)
            exit

print('horizontal:', horizontal, 'depth:', depth)
print(horizontal * depth)
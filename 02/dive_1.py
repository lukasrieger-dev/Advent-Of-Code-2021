horizontal = 0
depth = 0

with open('input.txt', 'r') as file:
    lines = file.readlines()
    instructions = (line.strip('\n') for line in lines)
    for instruction in instructions:
        command, value = instruction.split(' ')
        value = int(value)

        if command == 'forward':
            horizontal += value
        elif command == 'up':
            depth -= value
        elif command == 'down':
            depth += value
        else:
            print('Invalid command', command)
            exit

print('horizontal:', horizontal, 'depth:', depth)
print(horizontal * depth)
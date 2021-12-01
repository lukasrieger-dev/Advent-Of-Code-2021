import sys

current_depth = sys.maxsize
depth_increase = 0

with open('input.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        next_depth = int(line.strip('\n'))
        if current_depth - next_depth < 0:
            depth_increase += 1
        current_depth = next_depth

print(depth_increase)

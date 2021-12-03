lines = []
bit_pos = 0

with open('input.txt', 'r') as file:
    lines = [line.strip('\n') for line in file.readlines()]

while len(lines) > 1:
    column = []
    selected_lines = []
    for line in lines:
        bits = list(line.strip('\n'))
        column.append(bits[bit_pos])
    zeros = column.count('0')
    ones = column.count('1')
    criteria = '1' if ones >= zeros else '0'
    for line in lines:
        if line[bit_pos] == criteria:
            selected_lines.append(line)
    bit_pos += 1
    lines = selected_lines

oxygen = int(''.join(lines), 2)
print(oxygen)
#################################################
bit_pos = 0
with open('input.txt', 'r') as file:
    lines = [line.strip('\n') for line in file.readlines()]

while len(lines) > 1:
    column = []
    selected_lines = []
    for line in lines:
        bits = list(line.strip('\n'))
        column.append(bits[bit_pos])
    zeros = column.count('0')
    ones = column.count('1')
    criteria = '1' if ones < zeros else '0'
    for line in lines:
        if line[bit_pos] == criteria:
            selected_lines.append(line)
    bit_pos += 1
    lines = selected_lines

co2 = int(''.join(lines), 2)
print(co2)

print(oxygen * co2)
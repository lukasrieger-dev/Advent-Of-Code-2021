
gamma = []
epsilon = []
columns = []
lines = []

with open('input.txt', 'r') as file:
    lines = file.readlines()

columns_count = len(lines[0].strip('\n'))
for _ in range(columns_count):
    columns.append([])

for line in lines:
    bits = list(line.strip('\n'))
    for idx, bit in enumerate(bits):
        columns[idx].append(bit)

for column in columns:
    zeros = column.count('0')
    ones = column.count('1')
    if zeros > ones:
        gamma.append('0')
    else:
        gamma.append('1')

for bit in gamma:
    if bit == '0':
        epsilon.append('1')
    else:
        epsilon.append('0')

g = int(''.join(gamma), 2)
e = int(''.join(epsilon), 2)

print(g * e)
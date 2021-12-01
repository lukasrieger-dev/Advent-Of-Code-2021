import sys

sliding_window = []
SLIDING_WINDOW_SIZE = 3
last_sum = sys.maxsize
depth_increase = 0

with open('input.txt', 'r') as file:
    lines = file.readlines()
    sonar = (int(line.strip('\n')) for line in lines) 
    measurement = 0
    while (measurement := next(sonar, None)):   
        sliding_window.append(measurement)
        if len(sliding_window) < SLIDING_WINDOW_SIZE:
            continue
        
        window_sum = sum(sliding_window)
        if last_sum - window_sum < 0:
            depth_increase += 1
        last_sum = window_sum
        del sliding_window[0]

print(depth_increase)

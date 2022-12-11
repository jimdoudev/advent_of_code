from readlines import *

lines = [x.split(" ") for x in input_to_lines("day10.txt")]

cycle = 0

register_x = 1

signal_strength = [0 for x in range(6)]
signal_stoppers = [20, 60, 100, 140, 180, 220]
signal_index = 0


for line in lines:
    if line[0] == "noop":
        cycle += 1
        if(signal_stoppers[signal_index] == cycle):
            signal_strength[signal_index] = signal_stoppers[signal_index] * register_x
            signal_index += 1
    else:
        for x in range(2):
            cycle += 1
            if(signal_stoppers[signal_index] == cycle):
                signal_strength[signal_index] = signal_stoppers[signal_index] * register_x
                signal_index += 1
            if(x == 1):
                register_x += int(line[1])
    if(signal_index == 6):
        break

print(sum(signal_strength))

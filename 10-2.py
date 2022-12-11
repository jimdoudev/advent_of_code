from readlines import *

lines = [x.split(" ") for x in input_to_lines("day10.txt")]

def draw():
    if(len(crt_rows[curr_crt_row]) in sprite_range):
            crt_rows[curr_crt_row].append("#")
    else:
        crt_rows[curr_crt_row].append(".")

cycle = 0

register_x = 0
sprite_range = [register_x + x for x in range(3)]
crt_rows = [[] for x in range(6)]
curr_crt_row = 0

for line in lines:
    if line[0] == "noop":
        cycle += 1
        draw()
        if(cycle % 40 == 0):
            curr_crt_row += 1
    else:
        for x in range(2):
            cycle += 1
            draw()
            if(cycle % 40 == 0):
                curr_crt_row += 1
            if(x == 1):
                register_x += int(line[1])
                sprite_range = [register_x + x for x in range(3)]
    if(cycle == 240):
        break

for row in crt_rows:
    print("".join(row))


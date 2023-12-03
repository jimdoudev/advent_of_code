file = open("input.txt", "r")
Lines = file.readlines()

horizontal = 0
depth = 0
aim = 0

for line in Lines:
    direction = line.split(" ")[0]
    by = int(line.split(" ")[1])
    if direction == "forward":
        horizontal += by
        depth += (aim * by)
    elif direction == "up":
        aim -= by
    else:
        aim += by
            
print(horizontal * depth)
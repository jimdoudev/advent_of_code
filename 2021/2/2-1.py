file = open("input.txt", "r")
Lines = file.readlines()

horizontal = 0
vertical = 0

for line in Lines:
    direction = line.split(" ")[0]
    by = int(line.split(" ")[1])
    if direction == "forward":
        horizontal += by
    elif direction == "up":
        vertical -= by
    else:
        vertical += by
        
print(horizontal * vertical)
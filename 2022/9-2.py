from readlines import *

lines = [x.split(" ") for x in input_to_lines("day9.txt")]

def get_grid_size(input: List[str]) -> List[int]:
    max_udlr = [0, 0, 0, 0]
    sx = 0
    sy = 0
    for line in lines:
        match line[0]:
            case "U":
                sy += int(line[1])
                if(sy > 0 and abs(sy) > max_udlr[0]):
                    max_udlr[0] = abs(sy)
            case "D":
                sy -= int(line[1])
                if(sy < 0 and abs(sy) > max_udlr[1]):
                    max_udlr[1] = abs(sy)
            case "L":
                sx -= int(line[1])
                if(sx < 0 and abs(sx) > max_udlr[2]):
                    max_udlr[2] = abs(sx)
            case "R":
                sx += int(line[1])
                if(sx > 0 and abs(sx) > max_udlr[3]):
                    max_udlr[3] = abs(sx)
    return(max_udlr)

def create_grid(size: List[int]):
    size_y = size[0] + size[1] + 1
    size_x = size[2] + size[3] + 1
    grid = [[[] for x in range(0, size_x)] for y in range(0, size_y)]
    start_h = [size[0], size[2]]
    for x in range(0, 10):
        grid[start_h[0]][start_h[1]].append(x)
    return [grid, start_h]

def move(input: List[str]) -> None:
    for line in input:
        match line[0]:
            case "U":
                for x in range(0, int(line[1])):
                    for y in range(0, 10):
                        if(y == 0):
                            grid[indexes[y][0]][indexes[y][1]].remove(y)
                            indexes[y][0] -= 1
                            grid[indexes[y][0]][indexes[y][1]].append(y)
                        else:
                            if(abs(indexes[y - 1][0] - indexes[y][0]) > 1):
                                if(indexes[y - 1][1] == indexes[y][1]):
                                    grid[indexes[y][0]][indexes[y][1]].remove(y)
                                    indexes[y][0] -= 1
                                    grid[indexes[y][0]][indexes[y][1]].append(y)
                                elif(indexes[y - 1][1] > indexes[y][1]):
                                    grid[indexes[y][0]][indexes[y][1]].remove(y)
                                    if(indexes[y - 1][0] > indexes[y][0]):
                                        indexes[y][0] += 1
                                    elif(indexes[y - 1][0] < indexes[y][0]):
                                        indexes[y][0] -= 1
                                    indexes[y][1] += 1
                                    grid[indexes[y][0]][indexes[y][1]].append(y)
                                else:
                                    grid[indexes[y][0]][indexes[y][1]].remove(y)
                                    if(indexes[y - 1][0] > indexes[y][0]):
                                        indexes[y][0] += 1
                                    elif(indexes[y - 1][0] < indexes[y][0]):
                                        indexes[y][0] -= 1
                                    indexes[y][1] -= 1
                                    grid[indexes[y][0]][indexes[y][1]].append(y)
                            elif(abs(indexes[y - 1][1] - indexes[y][1]) > 1):
                                if(indexes[y - 1][1] > indexes[y][1]):
                                    grid[indexes[y][0]][indexes[y][1]].remove(y)
                                    if(indexes[y - 1][0] > indexes[y][0]):
                                        indexes[y][0] += 1
                                    elif(indexes[y - 1][0] < indexes[y][0]):
                                        indexes[y][0] -= 1
                                    indexes[y][1] += 1
                                    grid[indexes[y][0]][indexes[y][1]].append(y)
                                else:
                                    grid[indexes[y][0]][indexes[y][1]].remove(y)
                                    if(indexes[y - 1][0] > indexes[y][0]):
                                        indexes[y][0] += 1
                                    elif(indexes[y - 1][0] < indexes[y][0]):
                                        indexes[y][0] -= 1
                                    indexes[y][1] -= 1
                                    grid[indexes[y][0]][indexes[y][1]].append(y)
                        if(y == 9):
                            t_positions.add(tuple(indexes[9]))
            case "D":
                for x in range(0, int(line[1])):
                    for y in range(0, 10):
                        if(y == 0):
                            grid[indexes[y][0]][indexes[y][1]].remove(y)
                            indexes[y][0] += 1
                            grid[indexes[y][0]][indexes[y][1]].append(y)
                        else:
                            if(abs(indexes[y - 1][0] - indexes[y][0]) > 1):
                                if(indexes[y - 1][1] == indexes[y][1]):
                                    grid[indexes[y][0]][indexes[y][1]].remove(y)
                                    indexes[y][0] += 1
                                    grid[indexes[y][0]][indexes[y][1]].append(y)
                                elif(indexes[y - 1][1] > indexes[y][1]):
                                    grid[indexes[y][0]][indexes[y][1]].remove(y)
                                    if(indexes[y - 1][0] > indexes[y][0]):
                                        indexes[y][0] += 1
                                    elif(indexes[y - 1][0] < indexes[y][0]):
                                        indexes[y][0] -= 1
                                    indexes[y][1] += 1
                                    grid[indexes[y][0]][indexes[y][1]].append(y)
                                else:
                                    grid[indexes[y][0]][indexes[y][1]].remove(y)
                                    if(indexes[y - 1][0] > indexes[y][0]):
                                        indexes[y][0] += 1
                                    elif(indexes[y - 1][0] < indexes[y][0]):
                                        indexes[y][0] -= 1
                                    indexes[y][1] -= 1
                                    grid[indexes[y][0]][indexes[y][1]].append(y)
                            elif(abs(indexes[y - 1][1] - indexes[y][1]) > 1):
                                if(indexes[y - 1][1] > indexes[y][1]):
                                    grid[indexes[y][0]][indexes[y][1]].remove(y)
                                    if(indexes[y - 1][0] > indexes[y][0]):
                                        indexes[y][0] += 1
                                    elif(indexes[y - 1][0] < indexes[y][0]):
                                        indexes[y][0] -= 1
                                    indexes[y][1] += 1
                                    grid[indexes[y][0]][indexes[y][1]].append(y)
                                else:
                                    grid[indexes[y][0]][indexes[y][1]].remove(y)
                                    if(indexes[y - 1][0] > indexes[y][0]):
                                        indexes[y][0] += 1
                                    elif(indexes[y - 1][0] < indexes[y][0]):
                                        indexes[y][0] -= 1
                                    indexes[y][1] -= 1
                                    grid[indexes[y][0]][indexes[y][1]].append(y)
                        if(y == 9):
                            t_positions.add(tuple(indexes[9]))
            case "L":
                for x in range(0, int(line[1])):
                    for y in range(0, 10):
                        if(y == 0):
                            grid[indexes[y][0]][indexes[y][1]].remove(y)
                            indexes[y][1] -= 1
                            grid[indexes[y][0]][indexes[y][1]].append(y)
                        else:
                            if(abs(indexes[y - 1][1] - indexes[y][1]) > 1):
                                if(indexes[y - 1][0] == indexes[y][0]):
                                    grid[indexes[y][0]][indexes[y][1]].remove(y)
                                    indexes[y][1] -= 1
                                    grid[indexes[y][0]][indexes[y][1]].append(y)
                                elif(indexes[y - 1][0] > indexes[y][0]):
                                    grid[indexes[y][0]][indexes[y][1]].remove(y)
                                    if(indexes[y - 1][1] > indexes[y][1]):
                                        indexes[y][1] += 1
                                    elif(indexes[y - 1][1] < indexes[y][1]):
                                        indexes[y][1] -= 1
                                    indexes[y][0] += 1
                                    grid[indexes[y][0]][indexes[y][1]].append(y)
                                else:
                                    grid[indexes[y][0]][indexes[y][1]].remove(y)
                                    indexes[y][0] -= 1
                                    if(indexes[y - 1][1] > indexes[y][1]):
                                        indexes[y][1] += 1
                                    elif(indexes[y - 1][1] < indexes[y][1]):
                                        indexes[y][1] -= 1
                                    grid[indexes[y][0]][indexes[y][1]].append(y)
                            elif(abs(indexes[y - 1][0] - indexes[y][0]) > 1):
                                if(indexes[y - 1][0] > indexes[y][0]):
                                    grid[indexes[y][0]][indexes[y][1]].remove(y)
                                    indexes[y][0] += 1
                                    if(indexes[y - 1][1] > indexes[y][1]):
                                        indexes[y][1] += 1
                                    elif(indexes[y - 1][1] < indexes[y][1]):
                                        indexes[y][1] -= 1
                                    grid[indexes[y][0]][indexes[y][1]].append(y)
                                else:
                                    grid[indexes[y][0]][indexes[y][1]].remove(y)
                                    indexes[y][0] -= 1
                                    if(indexes[y - 1][1] > indexes[y][1]):
                                        indexes[y][1] += 1
                                    elif(indexes[y - 1][1] < indexes[y][1]):
                                        indexes[y][1] -= 1
                                    grid[indexes[y][0]][indexes[y][1]].append(y)
                        if(y == 9):
                            t_positions.add(tuple(indexes[9]))
            case "R":
                for x in range(0, int(line[1])):
                    for y in range(0, 10):
                        if(y == 0):
                            grid[indexes[y][0]][indexes[y][1]].remove(y)
                            indexes[y][1] += 1
                            grid[indexes[y][0]][indexes[y][1]].append(y)
                        else:
                            if(abs(indexes[y - 1][1] - indexes[y][1]) > 1):
                                if(indexes[y - 1][0] == indexes[y][0]):
                                    grid[indexes[y][0]][indexes[y][1]].remove(y)
                                    indexes[y][1] += 1
                                    grid[indexes[y][0]][indexes[y][1]].append(y)
                                elif(indexes[y - 1][0] > indexes[y][0]):
                                    grid[indexes[y][0]][indexes[y][1]].remove(y)
                                    indexes[y][0] += 1
                                    if(indexes[y - 1][1] > indexes[y][1]):
                                        indexes[y][1] += 1
                                    elif(indexes[y - 1][1] < indexes[y][1]):
                                        indexes[y][1] -= 1
                                    grid[indexes[y][0]][indexes[y][1]].append(y)
                                else:
                                    grid[indexes[y][0]][indexes[y][1]].remove(y)
                                    indexes[y][0] -= 1
                                    if(indexes[y - 1][1] > indexes[y][1]):
                                        indexes[y][1] += 1
                                    elif(indexes[y - 1][1] < indexes[y][1]):
                                        indexes[y][1] -= 1
                                    grid[indexes[y][0]][indexes[y][1]].append(y)
                            elif(abs(indexes[y - 1][0] - indexes[y][0]) > 1):
                                if(indexes[y - 1][0] > indexes[y][0]):
                                    grid[indexes[y][0]][indexes[y][1]].remove(y)
                                    indexes[y][0] += 1
                                    if(indexes[y - 1][1] > indexes[y][1]):
                                        indexes[y][1] += 1
                                    elif(indexes[y - 1][1] < indexes[y][1]):
                                        indexes[y][1] -= 1
                                    grid[indexes[y][0]][indexes[y][1]].append(y)
                                else:
                                    grid[indexes[y][0]][indexes[y][1]].remove(y)
                                    indexes[y][0] -= 1
                                    if(indexes[y - 1][1] > indexes[y][1]):
                                        indexes[y][1] += 1
                                    elif(indexes[y - 1][1] < indexes[y][1]):
                                        indexes[y][1] -= 1
                                    grid[indexes[y][0]][indexes[y][1]].append(y)
                        if(y == 9):
                            t_positions.add(tuple(indexes[9]))
                

starter_pack = create_grid(get_grid_size(lines))

grid = starter_pack[0]

indexes = []
for i in range(0, 10):
    indexes.append([starter_pack[1][0], starter_pack[1][1]])

t_positions = set()
t_positions.add(tuple(indexes[9]))

print(indexes[9])

move(lines)

print(len(t_positions))


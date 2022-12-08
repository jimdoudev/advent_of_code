from readlines import *

def check_y(input: str, index_y: int, index_x: int) -> List[int]:
    found = [-1, -1]
    for y in range(0, max_height):
        if(y < index_y and forest[y][index_x] >= input):
            found[0] = 1
        elif (y == index_y):
            continue
        elif(y > index_y and forest[y][index_x] >= input):
            found[1] = 1
        if(found[0] > 0 and found[1] > 0):
            break
    return found

def check_x(input: str, index_y: int, index_x: int) -> List[int]:
    found = [-1, -1]
    for x in range(0, max_width):
        if(x < index_x and forest[index_y][x] >= input):
            found[0] = 1
        elif (x == index_x):
            continue
        elif(x > index_x and forest[index_y][x] >= input):
            found[1] = 1
        if(found[0] > 0 and found[1] > 0):
            break
    return found

forest = [[y for y in x] for x in input_to_lines("day8.txt")]

max_width = len(forest[0])

max_height = len(forest)

grid_trees = 2 * (max_width - 2) + 2 * max_height

visible_trees = grid_trees

for y in range(1, max_width - 1):
    for x in range(1, max_height - 1):
        found_y = check_y(forest[y][x], y, x)
        found_x = check_x(forest[y][x], y, x)
        if(sum(found_x) <= 0 or sum(found_y) <= 0):
            visible_trees +=1
        

print(visible_trees)
from readlines import *

def check_y(input: str, index_y: int, index_x: int) -> List[int]:
    found = [-1, -1]
    for y in range(0, max_height):
        if(y < index_y and forest[y][index_x] >= input):
            found[0] = index_y - y
        elif (y == index_y):
            if(found[0] < 0):
                found[0] = index_y
            continue
        elif(y > index_y and forest[y][index_x] >= input):
            found[1] = y - index_y
            break
        if(y == max_height - 1 and found[1] < 0):
            found[1] = y - index_y
    return found

def check_x(input: str, index_y: int, index_x: int) -> List[int]:
    found = [-1, -1]
    for x in range(0, max_width):
        if(x < index_x and forest[index_y][x] >= input):
            found[0] = index_x - x
        elif (x == index_x):
            if(found[0] < 0):
                found[0] = index_x
            continue
        elif(x > index_x and forest[index_y][x] >= input):
            found[1] = x - index_x
            break
        if(x == max_width - 1 and found[1] < 0):
            found[1] = x - index_x
    return found

forest = [[y for y in x] for x in input_to_lines("day8.txt")]

max_width = len(forest[0])

max_height = len(forest)

scenic_score = 0

for y in range(3, max_width - 1):
    for x in range(2, max_height - 1):
        score_y = check_y(forest[y][x], y, x)
        score_x = check_x(forest[y][x], y, x)
        score = score_y[0] * score_y[1] * score_x[0] * score_x[1]
        if(score > scenic_score):
            scenic_score = score
        

print(scenic_score)
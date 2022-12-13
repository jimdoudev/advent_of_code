from collections import deque
from readlines import *

def find_starts_finish():
    starts = []
    for y in range(0, len(grid)):
        for x in range(0, len(grid[0])):
            if grid[y][x] == "S":
                grid[y][x] = "a"
                starts.append([y, x])
            elif grid[y][x] == "a":
                starts.append([y, x])
            elif grid[y][x] == "E":
                grid[y][x] = "z"
                finish = [y,x]
    return([starts, finish])

def move(counter:int):
    #move_up
    if(current_pos[0] != 0 and (grid[current_pos[0] - 1][current_pos[1]] <= grid[current_pos[0]][current_pos[1]] or ord(grid[current_pos[0] - 1][current_pos[1]]) - ord(grid[current_pos[0]][current_pos[1]]) == 1)):
        if tuple([current_pos[0] - 1, current_pos[1]]) not in visited:
            frontier.append([[current_pos[0] - 1, current_pos[1]], counter + 1])
            visited.add(tuple([current_pos[0] - 1, current_pos[1]]))
    #move_down
    if(current_pos[0] != len(grid) - 1 and (grid[current_pos[0] + 1][current_pos[1]] <= grid[current_pos[0]][current_pos[1]] or ord(grid[current_pos[0] + 1][current_pos[1]]) - ord(grid[current_pos[0]][current_pos[1]]) == 1)):
        if tuple([current_pos[0] + 1, current_pos[1]]) not in visited:
            frontier.append([[current_pos[0] + 1, current_pos[1]], counter + 1])
            visited.add(tuple([current_pos[0] + 1, current_pos[1]]))
    #move_left
    if(current_pos[1] != 0 and (grid[current_pos[0]][current_pos[1] - 1] <= grid[current_pos[0]][current_pos[1]] or ord(grid[current_pos[0]][current_pos[1] - 1]) - ord(grid[current_pos[0]][current_pos[1]]) == 1)):
        if tuple([current_pos[0], current_pos[1] - 1]) not in visited:
            frontier.append([[current_pos[0], current_pos[1] - 1], counter + 1])
            visited.add(tuple([current_pos[0], current_pos[1] - 1]))
    #move_right
    if(current_pos[1] != len(grid[0]) - 1 and (grid[current_pos[0]][current_pos[1] + 1] <= grid[current_pos[0]][current_pos[1]] or ord(grid[current_pos[0]][current_pos[1] + 1]) - ord(grid[current_pos[0]][current_pos[1]]) == 1)):
        if tuple([current_pos[0], current_pos[1] + 1]) not in visited:
            frontier.append([[current_pos[0], current_pos[1] + 1], counter + 1])
            visited.add(tuple([current_pos[0], current_pos[1] + 1]))

grid = [list(x) for x in input_to_lines("day12.txt")]
init = find_starts_finish()
starts = [x for x in init[0]]
finish = [init[1][0], init[1][1]]
visited = set()
frontier = deque()
for x in starts:
    visited.add(tuple(x))
    frontier.append([x, 0])
current_pos = []
pos_index = [[],0]

while len(frontier) > 0:
    pos_index = frontier.popleft()
    current_pos = pos_index[0]
    if [current_pos[0], current_pos[1]] == finish:
         print(pos_index)
         break
    else:
        move(pos_index[1])



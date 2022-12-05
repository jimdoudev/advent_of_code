from readlines import *

lines = input_to_lines("day5.txt")
stack_num = 0
stack_lines = []
stacks = []
begin_moves = 0

##get number of stacks
for line in lines:
    newline = line.split(" ")
    if (newline[1].isnumeric()):
        stack_num = line[len(line)-2]
        stacks = [[] for i in range(int(stack_num))]
        begin_moves += 2
        break
    stack_lines.append(newline)
    begin_moves +=1

##fill stacks
for line in stack_lines:
    column = 0
    step = 1
    for x in range(0, len(line), step):
        if (line[x] != ""):
            stacks[int(column)].insert(0, line[x])
            column += 1
        else:
            column += 0.25

moves = lines[begin_moves:len(lines)]

##make moves
for move in moves:
    split_moves = move.split(" ")
    crates = int(split_moves[1])
    from_stack = int(split_moves[3]) - 1
    to_stack = int(split_moves[5]) - 1
    moved = stacks[from_stack][-crates:]
    stacks[to_stack].extend(moved)
    del stacks[from_stack][-crates:]

final = ""
for stack in stacks:
    final += stack[-1:][0].replace("[", "").replace("]", "")
print(final)

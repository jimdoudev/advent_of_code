from readlines import *

lines = [x.split(",") for x in input_to_lines("day4.txt")]
counter = 0
for line in lines:
    newline = [line[0].split("-"), line[1].split("-")]
    if(int(newline[0][1])-int(newline[0][0]) <= int(newline[1][1])-int(newline[1][0])):
        if((int(newline[0][0]) >= int(newline[1][0])) and (int(newline[0][1]) <= int(newline[1][1]))):
            counter += 1
    else:
        if((int(newline[1][0]) >= int(newline[0][0])) and (int(newline[1][1]) <= int(newline[0][1]))):
            counter += 1

print(counter)


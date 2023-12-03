from readlines import *

lines = [x.split(",") for x in input_to_lines("day4.txt")]
counter = 0
for line in lines:
    newline = [line[0].split("-"), line[1].split("-")]
    low_0, high_0, low_1, high_1 = int(newline[0][0]), int(newline[0][1]), int(newline[1][0]), int(newline[1][1])
    first_set = set(range(low_0, high_0 + 1))
    second_set = set(range(low_1, high_1 + 1))
    if(first_set & second_set):
        counter += 1
print(counter)
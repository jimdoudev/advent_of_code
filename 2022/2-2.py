from readlines import *

cases = {
    "A": {"X":3, "Y":4, "Z":8},
    "B": {"X":1, "Y":5, "Z":9},
    "C": {"X":2, "Y":6, "Z":7},
}

lines = [x.split(" ") for x in input_to_lines("day2.txt")]

score_count = 0

for line in lines:
    score_count += cases[line[0]][line[1]] 
print(score_count)
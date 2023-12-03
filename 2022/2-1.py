from readlines import *

cases = {
    "A": {"X":4, "Y":8, "Z":3},
    "B": {"X":1, "Y":5, "Z":9},
    "C": {"X":7, "Y":2, "Z":6},
}

lines = [x.split(" ") for x in input_to_lines("day2.txt")]

score_count = 0

for line in lines:
    score_count += cases[line[0]][line[1]] 
print(score_count)
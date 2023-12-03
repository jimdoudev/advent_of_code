from readlines import *

calories = []
lines = input_to_string("day1.txt").split("\n\n")
for line in lines:
    newline = line.split("\n")
    calories.append(sum(input_to_int(newline)))
print (sorted(calories, reverse = True)[0])
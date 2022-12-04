from readlines import *

calories = []
lines = input_to_string("day1.txt").split("\n\n")
for line in lines:
    newline = line.split("\n")
    calories.append(sum(input_to_int(newline)))
sum_highest_cals = sum(sorted(calories, reverse = True)[0:3])
print (sum_highest_cals)
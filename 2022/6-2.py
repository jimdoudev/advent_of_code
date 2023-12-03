from readlines import *

lines = input_to_string("day6.txt")
for x in range(0, len(lines) - 15):
    substr = [x for x in lines[x:x + 14]]
    if(len(set(substr)) == 14):
        solution = (x + 14)
        break
print(solution)





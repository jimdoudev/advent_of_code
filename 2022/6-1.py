from readlines import *

lines = input_to_string("day6.txt")
for x in range(0, len(lines) - 5):
    substr = [x for x in lines[x:x + 4]]
    if(len(set(substr)) == 4):
        solution = (x + 4)
        break
print(solution)





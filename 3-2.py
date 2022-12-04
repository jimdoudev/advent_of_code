from readlines import *

lines = input_to_lines("day3.txt")

priority_sum = 0

for x in range(0, len(lines), 3):
    for letter in lines[x]:
        if (letter in lines[x + 1] and letter in lines[x + 2]):
            if(letter.isupper()):
                priority_sum += (ord(letter) - 38)
                break
            else:
                priority_sum += (ord(letter) - 96)
                break
 
print(priority_sum)

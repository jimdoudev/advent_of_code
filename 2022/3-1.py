from readlines import *

lines = input_to_lines("day3.txt")

priority_sum = 0

for line in lines:
    newline = [line[0:len(line)//2], line[len(line)//2:]]
    for letter in newline[0]:
        if letter in newline[1]:
            if(letter.isupper()):
                priority_sum += (ord(letter) - 38)
                break
            else:
                priority_sum += (ord(letter) - 96)
                break
 
print(priority_sum)

file = open("input1.txt", "r")
Lines = file.readlines()

counter = 0
for i in range(1, len(Lines)):
    if int(Lines[i]) > int(Lines[i - 1]):
        counter += 1
print(counter)
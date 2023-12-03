
file1 = open("input.txt", "r")
Lines = file1.readlines()

count=0

for line in Lines:
    lis = line.split(":")
    ran = lis[0].split("-")
    subran = ran[1].split(" ")
    search = subran.pop()
    ran[1] = subran[0]
        
    lower = ran[0]
    uppper = ran[1]
    temp_count=0
    for i in range(1, len(lis[1]) - 1):
        if search == lis[1][i]:
            temp_count += 1
    if temp_count >= int(lower) and temp_count <= int(uppper):
        count +=1


print(count)
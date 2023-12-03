
file1 = open("input.txt", "r")
Lines = file1.readlines()

count=0

for line in Lines:
    lis = line.split(": ")
    ran = lis[0].split("-")
    subran = ran[1].split(" ")
    search = subran.pop()
    ran[1] = subran[0]
        
    lower = int(ran[0])
    upper = int(ran[1])
    
    if not((lis[1][lower - 1] == search) and (lis[1][upper - 1] == search)):
        if (lis[1][lower - 1] == search) or (lis[1][upper - 1] == search):
            count += 1


print(count)
def base_to_dec(n, b):
    counter = 1
    final = 0
    for digit in n:
        final += int(digit) * (b ** (int(len(n) - counter)))
        counter += 1
    return final

file = open("input.txt", "r")
Lines = file.readlines()
newLines = []
for line in Lines:
    newLine = line.rstrip("\n")
    newLines.append(newLine)


oxygen = newLines
carbon = newLines
i = 0
j = 0



while len(oxygen) > 1:
    tmp_list_0s = []
    tmp_list_1s = []
    for line in oxygen:
        if line[i] == "0":
            tmp_list_0s.append(line)
        elif line[i] == "1":
            tmp_list_1s.append(line)
    if len(tmp_list_0s) > len(tmp_list_1s):
        oxygen = tmp_list_0s
    else:
        oxygen = tmp_list_1s
    i += 1
    
    
while len(carbon) > 1:
    tmp_list_0s = []
    tmp_list_1s = []
    for line in carbon:
        if line[j] == "0":
            tmp_list_0s.append(line)
        elif line[j] == "1":
            tmp_list_1s.append(line)
    if len(tmp_list_0s) <= len(tmp_list_1s):
        carbon = tmp_list_0s
    else:
        carbon = tmp_list_1s
    j += 1

            
print(base_to_dec(oxygen[0], 2) * base_to_dec(carbon[0], 2))

file = open("input1.txt", "r")
Lines = file.readlines()


slid_wind_list = []
for i in range (0, len(Lines)-2):
    slid_wind_list.append(int(Lines[i]) + int(Lines[i + 1]) + int(Lines[i + 2]))
    if i + 2 == Lines[-1]:
        break

counter = 0
for i in range(1, len(slid_wind_list)):
    if slid_wind_list[i] > slid_wind_list[i - 1]:
        counter += 1
print(counter)
from readlines import *

lines = input_to_lines("day13.txt")

def compare(left, right):
    fin = len(left) if len(left) >= len(right) else len(right)
    for y in range(fin):
        if y >= len(left):
            return True
        if y >= len(right):
            return False
        left_val = left[y]
        right_val = right[y]
        if isinstance(left_val, int) and isinstance(right_val, int):
            if left_val < right_val:
                return True
            elif left_val > right_val:
                return False
        else:
            if isinstance(left_val, int):
                left_val = [left_val]
            if isinstance(right_val, int):
                right_val = [right_val]
            deeper_check = compare(left_val, right_val)
            if deeper_check is not None:
                return deeper_check


pairs = []
for x in range(0, len(lines), 3):
    pairs.append([eval(lines[x]), eval(lines[x+1])])
    
indices = []
index = 0

for pair in pairs:
    index +=1
    if(compare(pair[0], pair[1])):
        indices.append(index)

print(sum(indices))


from readlines import *
from functools import cmp_to_key

lines = input_to_lines("day13.txt")

def compare(left, right):
    fin = len(left) if len(left) >= len(right) else len(right)
    for y in range(fin):
        if y >= len(left):
            return 1
        if y >= len(right):
            return -1
        left_val = left[y]
        right_val = right[y]
        if isinstance(left_val, int) and isinstance(right_val, int):
            if left_val < right_val:
                return 1
            elif left_val > right_val:
                return -1
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
    pairs.append(eval(lines[x]))
    pairs.append(eval(lines[x+1]))
pairs.append([[2]])
pairs.append([[6]])

final = sorted(pairs, key=cmp_to_key(compare), reverse=True)

print((final.index([[2]]) + 1) * (final.index([[6]]) + 1))
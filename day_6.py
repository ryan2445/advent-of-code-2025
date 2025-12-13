import re
from math import prod

with open("day_6_input.txt") as f:
    problems = [re.split(r"\s+", line.strip()) for line in f.readlines()]

ans = 0
rows = len(problems)
cols = len(problems[0])
for col in range(cols):
    nums = []
    operation = ""
    for row in range(rows):
        if row == rows - 1:
            operation = problems[row][col]
        else:
            nums.append(int(problems[row][col]))

    match operation:
        case "+":
            ans += sum(nums)
        case "*":
            ans += prod(nums)
        case _:
            print(f"unknown operation: {operation}")

print(ans)

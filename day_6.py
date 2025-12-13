import re
from math import prod

# Part 1
# with open("day_6_input.txt") as f:
#     problems = [re.split(r"\s+", line.strip()) for line in f.readlines()]
# ans = 0
# rows = len(problems)
# cols = len(problems[0])
# for col in range(cols):
#     nums = []
#     operation = ""
#     for row in range(rows):
#         if row == rows - 1:
#             operation = problems[row][col]
#         else:
#             nums.append(int(problems[row][col]))

#     match operation:
#         case "+":
#             ans += sum(nums)
#         case "*":
#             ans += prod(nums)
#         case _:
#             print(f"unknown operation: {operation}")

with open("day_6_input.txt") as f:
    lines = f.readlines()

operations_line = lines[-1]
left = 0
right = 0
problems = []
operations = []
while left < len(operations_line):
    operations.append(operations_line[left])
    right = left + 1
    while right < len(operations_line) and operations_line[right] == " ":
        right += 1
    col = []
    for row in range(len(lines) - 1):
        col.append(
            lines[row][left : right - (1 if right != len(operations_line) else 0)]
        )
    problems.append(col)
    left = right

ans = 0
for i, nums in enumerate(problems):
    cephalopod_nums = [0] * len(nums[0])
    for col in range(len(nums[0])):
        tens_power = 0
        for row in range(len(nums) - 1, -1, -1):
            if nums[row][col] != " ":
                cephalopod_nums[col] += int(nums[row][col]) * 10**tens_power
                tens_power += 1

    match operations[i]:
        case "+":
            ans += sum(cephalopod_nums)
        case "*":
            ans += prod(cephalopod_nums)
        case _:
            print(f"unknown operation: {operations[i]}")

print(ans)

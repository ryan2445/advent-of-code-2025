with open("day_5_input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]
    new_line = lines.index("")
    ranges = [
        [int(start), int(end)]
        for start, end in [line.split("-") for line in lines[:new_line]]
    ]
    ids = [int(id) for id in lines[new_line + 1 :]]

ans = 0

# Part 1
# for id in ids:
#     for start, end in ranges:
#         if start <= id <= end:
#             ans += 1
#             break

# Part 2
ranges.sort()
merged = []
for start, end in ranges:
    if not merged or merged[-1][1] < start:
        merged.append([start, end])
    else:
        merged[-1][1] = max(merged[-1][1], end)
for start, end in merged:
    ans += end - start + 1

print(ans)

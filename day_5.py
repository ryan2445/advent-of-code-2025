with open("day_5_input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]
    new_line = lines.index("")
    ranges = [
        [int(start), int(end)]
        for start, end in [line.split("-") for line in lines[:new_line]]
    ]
    ids = [int(id) for id in lines[new_line + 1 :]]

ans = 0

for id in ids:
    for start, end in ranges:
        if start <= id <= end:
            ans += 1
            break

print(ans)

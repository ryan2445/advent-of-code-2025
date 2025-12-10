with open("day_4_input.txt", "r") as f:
    rolls = [list(line.strip()) for line in f.readlines()]

adjacent = [(0, 1), (0, -1), (1, 0), (-1, 0)]
diagonal = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

m = len(rolls)
n = len(rolls[0])

ans = 0

for i in range(m):
    for j in range(n):
        if rolls[i][j] == ".":
            continue

        found = 0
        for change_x, change_y in [*adjacent, *diagonal]:
            new_x = i + change_x
            new_y = j + change_y
            if 0 <= new_x < m and 0 <= new_y < n and rolls[new_x][new_y] == "@":
                found += 1

        if found < 4:
            ans += 1

print(ans)

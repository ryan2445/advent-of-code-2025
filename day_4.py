from collections import deque

with open("day_4_input.txt", "r") as f:
    rolls = [list(line.strip()) for line in f.readlines()]

adjacent = [(0, 1), (0, -1), (1, 0), (-1, 0)]
diagonal = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

m = len(rolls)
n = len(rolls[0])

ans = 0

# Part 1
# for i in range(m):
#     for j in range(n):
#         if rolls[i][j] == ".":
#             continue
#         found = 0
#         for change_x, change_y in [*adjacent, *diagonal]:
#             new_x = i + change_x
#             new_y = j + change_y
#             if 0 <= new_x < m and 0 <= new_y < n and rolls[new_x][new_y] == "@":
#                 found += 1
#         if found < 4:
#             ans += 1

# Part 2
neighbors = [[0] * n for _ in range(m)]
visited = [[False] * n for _ in range(m)]
queue = deque([])

for i in range(m):
    for j in range(n):
        if rolls[i][j] == ".":
            continue
        for change_x, change_y in [*adjacent, *diagonal]:
            new_x = i + change_x
            new_y = j + change_y
            if 0 <= new_x < m and 0 <= new_y < n and rolls[new_x][new_y] == "@":
                neighbors[i][j] += 1
        if neighbors[i][j] < 4:
            queue.append((i, j))

while queue:
    x, y = queue.popleft()
    if visited[x][y]:
        continue
    visited[x][y] = True
    ans += 1
    for change_x, change_y in [*adjacent, *diagonal]:
        new_x = x + change_x
        new_y = y + change_y
        if 0 <= new_x < m and 0 <= new_y < n and rolls[new_x][new_y] == "@":
            neighbors[new_x][new_y] -= 1
            if neighbors[new_x][new_y] < 4 and not visited[new_x][new_y]:
                queue.append((new_x, new_y))

print(ans)

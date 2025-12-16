from collections import deque

with open("day_9_input.txt") as f:
    red_coords = [list(map(int, line.strip().split(","))) for line in f.readlines()]

# Part 1
# max_rectangle_area = 0
# for i in range(len(red_coords)):
#     for j in range(i + 1, len(red_coords)):
#         x1, y1 = red_coords[i]
#         x2, y2 = red_coords[j]
#         width = abs(x1 - x2) + 1
#         height = abs(y1 - y2) + 1
#         max_rectangle_area = max(max_rectangle_area, width * height)
# print(max_rectangle_area)


def coordinate_compression(coords):
    x_coords = sorted(list(set(x for x, _ in coords)))
    y_coords = sorted(list(set(y for _, y in coords)))
    x_to_idx = {x: i for i, x in enumerate(x_coords)}
    y_to_idx = {y: i for i, y in enumerate(y_coords)}
    compressed = [(x_to_idx[x], y_to_idx[y]) for x, y in coords]
    return compressed, x_to_idx, y_to_idx


def draw_line(x1, y1, x2, y2):
    if x1 == x2:
        for y in range(min(y1, y2) + 1, max(y1, y2)):
            grid[y][x1] = "X"  # green
    elif y1 == y2:
        for x in range(min(x1, x2) + 1, max(x1, x2)):
            grid[y1][x] = "X"  # green


def flood(x, y, flood_value, grid):
    queue = deque([(x, y)])
    while queue:
        x, y = queue.popleft()
        if grid[y][x] == flood_value:
            continue
        grid[y][x] = flood_value
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_x = x + dx
            new_y = y + dy
            if (
                0 <= new_x < len(grid[0])
                and 0 <= new_y < len(grid)
                and grid[new_y][new_x] == "."
            ):
                queue.append((new_x, new_y))


def write_grid(grid):
    with open("day_9_output_grid.txt", "w") as f:
        for row in grid:
            f.write("".join(row) + "\n")


# Compress coordinates to create reasonably sized grid
compressed, x_to_idx, y_to_idx = coordinate_compression(red_coords)
max_x = max(x for x, _ in compressed)
max_y = max(y for _, y in compressed)
grid = [["."] * (max_x + 1) for _ in range(max_y + 1)]

# Mark red tiles and connect red tiles with green tiles
for i, (x, y) in enumerate(compressed):
    grid[y][x] = "#"  # red
    last_x, last_y = compressed[i - 1]
    draw_line(last_x, last_y, x, y)
    next_x, next_y = compressed[(i + 1) % len(compressed)]
    draw_line(x, y, next_x, next_y)

# Flood the outside of the polygon so we can easily find a point inside the polygon
# Assuming the polygon never enters the 4 corners of the grid
flood(0, 0, "-", grid)
flood(max_x, max_y, "-", grid)
flood(0, max_y, "-", grid)
flood(max_x, 0, "-", grid)

inside_x, inside_y = None, None
for y in range(max_y):
    for x in range(max_x):
        if grid[y][x] == ".":
            inside_x, inside_y = x, y
            break
    if inside_x is not None and inside_y is not None:
        break

# flood inside with green
flood(inside_x, inside_y, "X", grid)

max_area_red_green = 0
for i in range(len(red_coords)):
    for j in range(i + 1, len(red_coords)):
        x1, y1 = red_coords[i]
        x2, y2 = red_coords[j]

        x1_compressed, y1_compressed = x_to_idx[x1], y_to_idx[y1]
        x2_compressed, y2_compressed = x_to_idx[x2], y_to_idx[y2]

        valid = True
        for y in range(
            min(y1_compressed, y2_compressed), max(y1_compressed, y2_compressed) + 1
        ):
            for x in range(
                min(x1_compressed, x2_compressed), max(x1_compressed, x2_compressed) + 1
            ):
                if grid[y][x] == "-":
                    valid = False
                    break
            if not valid:
                break

        if valid:
            width = abs(x1 - x2) + 1
            height = abs(y1 - y2) + 1
            max_area_red_green = max(max_area_red_green, width * height)

write_grid(grid)
print(max_area_red_green)

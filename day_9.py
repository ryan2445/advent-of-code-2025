with open("day_9_input.txt") as f:
    tile_coordinates = [
        list(map(int, line.strip().split(","))) for line in f.readlines()
    ]

max_rectangle_area = 0
for i in range(len(tile_coordinates)):
    for j in range(i + 1, len(tile_coordinates)):
        x1, y1 = tile_coordinates[i]
        x2, y2 = tile_coordinates[j]
        width = abs(x1 - x2) + 1
        height = abs(y1 - y2) + 1
        max_rectangle_area = max(max_rectangle_area, width * height)
print(max_rectangle_area)

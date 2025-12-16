from collections import Counter
from math import prod

with open("day_8_input.txt") as f:
    coordinates = [list(map(int, line.strip().split(","))) for line in f.readlines()]
    num_coordinates = len(coordinates)


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False
        if root_x < root_y:
            self.parent[root_x] = root_y
        else:
            self.parent[root_y] = root_x
        return True


def euclidean_distance(x1, y1, z1, x2, y2, z2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2) ** 0.5


distances = []
for i in range(num_coordinates):
    for j in range(i + 1, num_coordinates):
        x1, y1, z1 = coordinates[i]
        x2, y2, z2 = coordinates[j]
        distance = euclidean_distance(x1, y1, z1, x2, y2, z2)
        distances.append((distance, i, j))
distances.sort()

directly_connected = set()
uf = UnionFind(num_coordinates)
connections_to_make = 1000
for _, i, j in distances:
    if connections_to_make == 0:
        break
    if (i, j) in directly_connected or (j, i) in directly_connected:
        continue
    directly_connected.add((i, j))
    connections_to_make -= 1
    uf.union(i, j)

roots = [uf.find(i) for i in range(num_coordinates)]
sizes = sorted(Counter(roots).values(), reverse=True)
top_3_product = prod(sizes[:3])
print(top_3_product)

from collections import defaultdict


with open("day_11_input.txt") as f:
    lines = [line.strip() for line in f.readlines()]
    graph = defaultdict(set)
    for line in lines:
        nodes = line.split(" ")
        source = nodes[0].removesuffix(":")
        destinations = nodes[1:]
        for destination in destinations:
            graph[source].add(destination)


def unique_paths(graph, start, end):
    if start == end:
        return 1

    ans = 0

    for neighbor in graph[start]:
        ans += unique_paths(graph, neighbor, end)

    return ans


print(unique_paths(graph, "you", "out"))

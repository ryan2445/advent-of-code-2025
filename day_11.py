from collections import defaultdict
from time import sleep


with open("day_11_input.txt") as f:
    lines = [line.strip() for line in f.readlines()]
    graph = defaultdict(set)
    for line in lines:
        nodes = line.split(" ")
        source = nodes[0].removesuffix(":")
        destinations = nodes[1:]
        for destination in destinations:
            graph[source].add(destination)


def unique_paths(graph, start, end, has_dac, has_fft, memo):
    if (start, has_dac, has_fft) in memo:
        return memo[(start, has_dac, has_fft)]

    if start == end:
        if has_dac and has_fft:
            return 1
        return 0

    ans = 0

    for neighbor in graph[start]:
        ans += unique_paths(
            graph,
            neighbor,
            end,
            neighbor == "dac" or has_dac,
            neighbor == "fft" or has_fft,
            memo,
        )

    memo[(start, has_dac, has_fft)] = ans
    return ans


memo = {}
print(unique_paths(graph, "svr", "out", False, False, memo))

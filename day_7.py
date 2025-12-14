with open("day_7_input.txt") as f:
    manifold = [list(line.strip()) for line in f.readlines()]
    start_i = 0
    start_j = manifold[0].index("S")


# Part 1
# def dfs_helper(i, j, visited):
#     if i < 0 or j < 0 or i >= len(manifold) or j >= len(manifold[0]):
#         return 0

#     if (i, j) in visited:
#         return 0
#     visited.add((i, j))

#     ans = 0

#     if manifold[i][j] == "^":
#         ans += 1
#         ans += dfs_helper(i, j - 1, visited)
#         ans += dfs_helper(i, j + 1, visited)
#     else:
#         ans += dfs_helper(i + 1, j, visited)

#     return ans

# print(dfs_helper(start_i, start_j, set()))


# Part 2
def dfs_helper(i, j, memo):
    if i == len(manifold) - 1:
        return 1

    if i < 0 or j < 0 or j >= len(manifold[0]):
        return 0

    if (i, j) in memo:
        return memo[(i, j)]

    if manifold[i][j] == "^":
        ans = dfs_helper(i, j - 1, memo) + dfs_helper(i, j + 1, memo)
    else:
        ans = dfs_helper(i + 1, j, memo)

    memo[(i, j)] = ans
    return ans


print(dfs_helper(start_i, start_j, {}))

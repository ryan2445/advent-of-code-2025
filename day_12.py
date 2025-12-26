with open("day_12_input.txt") as f:
    lines = [line.strip() for line in f.readlines()]

    patterns = []
    curr_pattern = []
    row, col = 0, 0
    for i, line in enumerate(lines[1:30]):
        if len(line) == 2:
            continue
        if not line:
            row, col = 0, 0
            patterns.append(curr_pattern)
            curr_pattern = []
            continue
        for char in line:
            if char == "#":
                curr_pattern.append((row, col))
            col += 1
        row += 1
        col = 0

    problems = []
    for problem in lines[31:]:
        for i, part in enumerate(problem.split(" ")):
            if i == 0:
                width, height = part.removesuffix(":").split("x")
                problems.append([int(width), int(height), []])
            else:
                problems[-1][2].append(int(part))

ans = 0
for problem in problems:
    width, height, counts = problem
    yes_fit = 0
    no_fit = 0
    maybe_fit = 0
    min_space = sum(len(pattern) * count for pattern, count in zip(patterns, counts))
    if min_space > width * height:
        no_fit += 1
    elif sum(counts) <= (width // 3) * (height // 3):
        yes_fit += 1
        ans += 1
    else:
        maybe_fit += 1


print(ans)

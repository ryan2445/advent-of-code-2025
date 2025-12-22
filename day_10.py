from collections import deque
from math import inf


def to_mask(chars):
    m = 0
    for i, c in enumerate(chars):
        if c == "#":
            m |= 1 << i
    return m


with open("day_10_input.txt") as f:
    lines = [line.strip() for line in f.readlines()]
    machines = []
    for line in lines:
        machine = {"target": 0, "buttons": [], "joltage": []}
        sections = line.split(" ")
        for section in sections:
            if section.startswith("["):
                end = section.index("]")
                machine["target"] = to_mask(section[1:end])
            elif section.startswith("("):
                end = section.index(")")
                button = section[1:end]
                machine["buttons"].append(list(map(int, button.split(","))))
            elif section.startswith("{"):
                end = section.index("}")
                joltage = section[1:end]
                machine["joltage"] = list(map(int, joltage.split(",")))
        machines.append(machine)


def fewest_button_presses(curr, target, button_masks):
    presses = {curr: 0}
    queue = deque([curr])

    while queue:
        state = queue.popleft()

        if state == target:
            return presses[state]

        for button_mask in button_masks:
            next = state ^ button_mask
            if next not in presses:
                presses[next] = presses[state] + 1
                queue.append(next)

    return inf


ans = 0
for machine in machines:
    button_masks = []
    for button in machine["buttons"]:
        button_mask = 0
        for idx in button:
            button_mask ^= 1 << idx
        button_masks.append(button_mask)

    ans += fewest_button_presses(0, machine["target"], button_masks)

print(ans)

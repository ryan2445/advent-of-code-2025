from collections import deque, Counter, defaultdict
from math import inf


def light_mask(chars):
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
                machine["target"] = light_mask(section[1:end])
            elif section.startswith("("):
                end = section.index(")")
                button = section[1:end]
                machine["buttons"].append(list(map(int, button.split(","))))
            elif section.startswith("{"):
                end = section.index("}")
                joltage = section[1:end]
                machine["joltage"] = list(map(int, joltage.split(",")))
        machines.append(machine)

# Part 1
# def fewest_button_presses(curr, target, button_masks):
#     presses = {curr: 0}
#     queue = deque([curr])

#     while queue:
#         state = queue.popleft()

#         if state == target:
#             return presses[state]

#         for button_mask in button_masks:
#             next = state ^ button_mask
#             if next not in presses:
#                 presses[next] = presses[state] + 1
#                 queue.append(next)

#     return inf


# ans = 0
# for machine in machines:
#     button_masks = []
#     for button in machine["buttons"]:
#         button_mask = 0
#         for idx in button:
#             button_mask ^= 1 << idx
#         button_masks.append(button_mask)

#     ans += fewest_button_presses(0, machine["target"], button_masks)

# print(ans)


# Figure out which joltage index is modified by the least number of buttons.
# Looking at the least used joltage indexes first reduces the number of recursive calls.
# When there are multiple buttons that modify the same joltage index, we should look at the button that modifies the most joltages first.
def sort_buttons(buttons):
    sorted_buttons = []
    while buttons:
        joltage_indices = []
        for button in buttons:
            joltage_indices.extend(button)

        joltage_counter = Counter(joltage_indices)
        least_used_joltage_idx = inf
        min_joltage_count = inf
        for joltage_idx, count in joltage_counter.items():
            if count < min_joltage_count:
                min_joltage_count = count
                least_used_joltage_idx = joltage_idx

        curr_button = None
        for button in buttons:
            if least_used_joltage_idx in button and (
                curr_button is None or len(button) > len(curr_button)
            ):
                curr_button = button

        sorted_buttons.append(curr_button)
        buttons.remove(curr_button)

    return sorted_buttons


# Track the last (greatest) button index that modifies a given joltage index.
def get_joltage_to_last_button_idx(sorted_buttons):
    joltage_to_last_button_idx = defaultdict(int)
    for button_idx, button in enumerate(sorted_buttons):
        for joltage_idx in button:
            joltage_to_last_button_idx[joltage_idx] = button_idx
    return joltage_to_last_button_idx


def dfs(remaining, button_idx, buttons, joltage_to_last_button_idx, presses, best):
    # If the presses so far are greater than the best so far, we can't do better
    if presses >= best:
        return best
    # If the remaining joltage requires more presses than the best so far, we can't do better
    if presses + max(remaining) >= best:
        return best

    if button_idx == len(buttons):
        if all(r == 0 for r in remaining):
            return min(best, presses)
        return best

    min_presses = 0
    max_presses = inf
    for joltage_idx in buttons[button_idx]:
        # We can only press up to the smallest remaining amount of joltage for a given button
        max_presses = min(max_presses, remaining[joltage_idx])
        # If this is the last button that can be used for this joltage, we need to press at least 'remaining' times
        if joltage_to_last_button_idx[joltage_idx] == button_idx:
            min_presses = max(min_presses, remaining[joltage_idx])

    if min_presses > max_presses:
        return best

    for to_press in range(min_presses, max_presses + 1):
        new_remaining = remaining.copy()
        for joltage_idx in buttons[button_idx]:
            new_remaining[joltage_idx] -= to_press
        best = dfs(
            new_remaining,
            button_idx + 1,
            buttons,
            joltage_to_last_button_idx,
            presses + to_press,
            best,
        )

    return best


ans = 0
for i, machine in enumerate(machines):
    buttons = sort_buttons(machine["buttons"])
    joltage_to_last_button_idx = get_joltage_to_last_button_idx(buttons)
    remaining = machine["joltage"]
    presses = dfs(remaining, 0, buttons, joltage_to_last_button_idx, 0, inf)
    ans += presses
    print(f"Machine {i}: {presses}")

print(f"Part 2: {ans}")

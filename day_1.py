
with open('day_1_input.txt', 'r') as f:
    rotations = [line.strip() for line in f.readlines()]

ans = 0
start = 50

for rotation in rotations:
  direction = rotation[0]
  distance = int(rotation[1:])

  if direction == 'R':
    start += distance
    start %= 100
  elif direction == 'L':
    start -= distance
    start += 100
    start %= 100

  if start == 0:
    ans += 1

print(ans)


with open('day_1_input.txt', 'r') as f:
    rotations = [line.strip() for line in f.readlines()]

ans = 0
curr_pos = 50

for rotation in rotations:
  direction = rotation[0]
  distance = int(rotation[1:])

  full_rotations = distance // 100
  ans += full_rotations
  distance %= 100

  if direction == 'R':
    if curr_pos + distance >= 100:
      ans += 1
    curr_pos += distance
    curr_pos %= 100
  elif direction == 'L':
    if curr_pos != 0 and curr_pos - distance <= 0:
      ans += 1
    curr_pos -= distance
    curr_pos += 100
    curr_pos %= 100

print(ans)

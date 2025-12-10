
with open('day_3_input.txt', 'r') as f:
  banks = [line.strip() for line in f.readlines()]

ans = 0

for bank in banks:
  bank = list(bank)

  # Part 1
  # first_digit = bank[0]
  # second_digit = bank[1]
  # for i in range(2, len(bank)):
  #   if i < len(bank) - 1 and bank[i] > first_digit:
  #     first_digit = bank[i]
  #     second_digit = bank[i + 1]
  #   elif bank[i] > second_digit:
  #     second_digit = bank[i]
  # ans += int(first_digit + second_digit)

  # Part 2
  stack = []
  poppable = len(bank) - 12
  for digit in bank:
    while stack and stack[-1] < digit and poppable > 0:
      stack.pop()
      poppable -= 1
    stack.append(digit)
  ans += int(''.join(stack[:12]))

print(ans)

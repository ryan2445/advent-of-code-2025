
with open('day_2_input.txt', 'r') as f:
  ranges = f.readline().split(',')

ans = 0

for range_str in ranges:
  start, end = range_str.split('-')
  
  for i in range(int(start), int(end) + 1):
    str_i = str(i)

    # Part 1    
    # middle = len(str_i) // 2
    # left = str_i[:middle]
    # right = str_i[middle:]
    # if left == right:
    #   ans += i

    # Part 2
    seq_len = 1
    while seq_len <= len(str_i) // 2:
      if all(str_i[:seq_len] == str_i[j:j+seq_len] for j in range(0, len(str_i), seq_len)):
        ans += i
        break
      seq_len += 1

print(ans)

s = input().strip()

current = 'a'
total_moves = 0

for c in s:
    diff = abs(ord(c) - ord(current))
    total_moves += min(diff, 26 - diff)
    current = c

print(total_moves)

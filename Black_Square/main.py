cost = list(map(int, input().split()))
s = input().strip()

total = 0
for c in s:
    total += cost[int(c)-1]

print(total)

n = int(input())

count = 0

for _ in range(n):
    friends = list(map(int, input().split()))
    if sum(friends) >= 2:
        count += 1

print(count)

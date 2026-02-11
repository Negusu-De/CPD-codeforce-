n = int(input())
events = list(map(int, input().split()))

available = 0
untreated = 0

for event in events:
    if event > 0:
        available += event
    elif event == -1:
        if available > 0:
            available -= 1
        else:
            untreated += 1

print(untreated)

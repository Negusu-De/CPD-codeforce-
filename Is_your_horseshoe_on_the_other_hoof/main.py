colors = list(map(int, input().split()))

distinct = len(set(colors))

print(4 - distinct)

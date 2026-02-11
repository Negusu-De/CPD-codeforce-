username = input().strip()

distinct_letters = set(username)

if len(distinct_letters) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")

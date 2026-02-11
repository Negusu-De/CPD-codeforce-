n = int(input())
cards = list(map(int, input().split()))

s_score, d_score = 0, 0
left, right = 0, n - 1
turn = 0

while left <= right:
    if cards[left] >= cards[right]:
        chosen = cards[left]
        left += 1
    else:
        chosen = cards[right]
        right -= 1

    if turn == 0:
        s_score += chosen
    else:
        d_score += chosen

    turn = 1 - turn

print(s_score, d_score)

import sys
N = int(sys.stdin.readline())
card = {}
for _ in range(N):
    x = int(sys.stdin.readline())
    if x not in card :
        card[x] = 1
    else:
        card[x] += 1

n = max(card.values())
for i in sorted(card):
    if n == card[i] :
        print(i)
        break
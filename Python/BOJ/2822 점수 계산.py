import sys
num = sorted([[int(sys.stdin.readline()),i] for i in range(1,9)], reverse=True)
result = 0
rank = []
for score, i in num[:5]:
    result += score
    rank.append(i)
print(result)
print(*sorted(rank))
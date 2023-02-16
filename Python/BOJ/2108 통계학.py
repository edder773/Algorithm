import sys
from collections import Counter
N = int(sys.stdin.readline())
P = [0]*N

for value in range(N):
    P[value] = int(sys.stdin.readline())

P = sorted(P)
O = set(P)
cnt = 0
print(round(sum(P)/N))
print(P[len(P)//2])
temp = Counter(P).most_common()
if len(temp) > 1 and temp[0][1] == temp[1][1]:
    print(temp[1][0])
else:
    print(temp[0][0])

print(max(P)-min(P))

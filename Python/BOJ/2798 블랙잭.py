import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
card = deque(map(int, sys.stdin.readline().split()))
cnt = 0
for i in range(N):
    for j in range(N):
        for k in range(N):
            if i != j and i != k and j != k:
                sum = card[i]+card[j]+card[k]
                if sum >= cnt and sum <= M:
                    cnt = sum
print(cnt)

import sys

N, M = map(int, sys.stdin.readline().split())
lecture = []
for k in range(N):
    P, L = map(int, sys.stdin.readline().split())
    m = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)
    if P < L:
        lecture.append(1)
    else:
        lecture.append(m[L - 1])

lecture.sort()
result = 0
for i in lecture:
    if M >= i:
        result += 1
        M -= i
print(result)

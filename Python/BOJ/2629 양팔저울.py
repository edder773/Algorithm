import sys
N = int(sys.stdin.readline())
weight = list(map(int, sys.stdin.readline().split()))
M = list(sys.stdin.readline())
bead = list(map(int, sys.stdin.readline().split()))

dp = [0]
for i in weight:
    temp=[]
    for j in dp:
        temp += [i+j, abs(i-j)]
    dp = list(set(dp + temp))

result = []
for i in bead:
    if i in dp:
        result.append('Y')
    else:
        result.append('N')
print(*result)
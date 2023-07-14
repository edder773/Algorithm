import sys
N = list(map(int, sys.stdin.readline().strip()))
R = map(int, sys.stdin.readline().strip())
result = []
ncnt = [0] * 10
ecnt = [0] * 10

for i in N: 
    ncnt[i] += 1

for i in R:
    ecnt[i] += 1

for i in N:
    if ecnt[i] and ecnt[i] == ncnt[i]:
        ncnt[i] -= 1
        ecnt[i] -= 1
    else :
        while result:
            if result[-1] >= i or not ecnt[result[-1]]:
                break
            ecnt[result[-1]] -= 1
            result.pop()
        ncnt[i] -= 1
        result.append(i)
if ecnt[result[-1]]:
    result.pop()
print(*result, sep= "")
import sys
N, K = map(int, sys.stdin.readline().split())
table = list(sys.stdin.readline().strip())
result = 0
for i in range(N):
    if table[i] == 'P' :
        for x in range(max(i-K,0), min(i+K+1,N)):
            if table[x] == 'H':
                table[x] = 'ATE'
                result += 1
                break
print(result)
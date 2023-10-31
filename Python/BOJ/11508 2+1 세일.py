import sys
N = int(sys.stdin.readline())
milk = sorted([int(sys.stdin.readline()) for _ in range(N)],reverse=True)
result = 0
print(milk)
for i in range(N):
    if (i+1) % 3 :
        result += milk[i]
print(result)
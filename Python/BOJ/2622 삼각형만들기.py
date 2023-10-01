import sys
N = int(sys.stdin.readline())
result = 0
for i in range((N+1)//3, (N+1)//2):
    result += (3*i - N + 2)//2
print(result)
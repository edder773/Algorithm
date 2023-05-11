import sys
N = int(sys.stdin.readline())
result = 0
for i in range(1,N+1):
    result += N/i
print(result)
import sys
N = int(sys.stdin.readline())
num = sorted([int(sys.stdin.readline()) for _ in range(N)])

for i in range(N-1,-1,-1):
    print(num[i])
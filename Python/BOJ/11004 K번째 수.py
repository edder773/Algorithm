import sys
N, K = map(int, sys.stdin.readline().split())
A = sorted(list(map(int, sys.stdin.readline().split())))
print(A[K-1])
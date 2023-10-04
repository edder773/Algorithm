import sys
nA, nB = map(int, sys.stdin.readline().split())
A = set(map(int, sys.stdin.readline().split()))
B = set(map(int, sys.stdin.readline().split()))
AnB = A-B
print(len(AnB))
if (AnB):
    print(*sorted(AnB))
import sys
from itertools import permutations
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
result = 0
for i in permutations(A):
    temp = 0
    for x in range(N-1):
        temp += abs(i[x] - i[x+1])
    result = max(result, temp)
print(result)
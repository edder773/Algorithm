import sys
from itertools import combinations
N = int(sys.stdin.readline())
students = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
num, winner = 0, 0
for i in range(N):
    for x in combinations(students[i],3):
        a = sum(x) % 10
        if num <= a:
            num = a
            winner = i + 1
print(winner)
import sys
N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
censer = sorted(list(map(int, sys.stdin.readline().split())))
x = []
for i in range(N-1):
    x += [censer[i+1] - censer[i]] # 각센서 간의 차이
x.sort()
print(sum(x[:N-K]))
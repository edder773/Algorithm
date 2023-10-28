import sys
K = int(sys.stdin.readline())
a, b = 1, 0
for i in range(K):
    a, b = b, a+b
print(a,b)
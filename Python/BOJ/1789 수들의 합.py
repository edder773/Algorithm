import sys
S = int(sys.stdin.readline())
n = 0
while (n**2 + n)//2 <= S:
    n += 1
print(n-1)
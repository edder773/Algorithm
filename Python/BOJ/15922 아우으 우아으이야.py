import sys
N = int(sys.stdin.readline())
m, p = map(int, sys.stdin.readline().split())
result = p - m 
for _ in range(N-1):
    a, b = map(int,sys.stdin.readline().split())
    if a <= p and b > p:
        result += b - p
        p = b
    elif a > p :
        result += b - a
        m, p = a, b
print(result)
def f(n):
    if n >= 2 and len(x) <= n:
        x.append(f(n-2)+f(n-1))   
    return x[n]
import sys
N = int(sys.stdin.readline())
x = [0,1]
print(f(N))
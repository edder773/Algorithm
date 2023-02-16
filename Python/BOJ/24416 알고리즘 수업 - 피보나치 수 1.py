import sys
cnt = 1


def fib(n):
    global cnt
    if n == 1 or n == 2:
        return 1
    else:
        cnt += 1
        return (fib(n-1)+fib(n-2))


d = [0]*42
d[1] = 1
d[2] = 1
cnt2 = 0
N = int(sys.stdin.readline())
for i in range(3, N+1):
    cnt2 += 1
    d[i] = d[i-1]+d[i-2]
fib(N)
print(cnt, cnt2)

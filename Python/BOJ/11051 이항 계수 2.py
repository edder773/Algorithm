import sys
N, K = map(int, sys.stdin.readline().split())
sys.setrecursionlimit(1000*100)


def f(n):
    if n == 0:
        return 1
    return f(n-1)*n


cnt = 0


def p(n, m):
    global cnt
    cnt += 1
    if m == 0:
        return 1
    if m == cnt:
        return n
    return p(n-1, m)*n


print((p(N, K)//f(K)) % 10007)

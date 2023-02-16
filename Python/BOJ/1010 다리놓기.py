T = int(input())
for _ in range(T):
    N, M = map(int, input().split())

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

    print(p(M, N)//f(N))

T = int(input())


def abs_n(n):
    if n >= 0:
        return n
    elif n < 0:
        return -n


for case in range(1, T+1):
    N = int(input())
    s = [0]*N
    for i in range(N):
        s[i] = list(map(int, input().split()))
    di = [0, 0, -1, 1]
    dj = [-1, 1, 0, 0]
    ni = nj = 0
    sums = 0
    for i in range(N):
        for j in range(N):
            for k in range(4):
                ni, nj = i + di[k], j + dj[k]
                if 0 <= ni < N and 0 <= nj < N:
                    sums += abs_n(s[i][j]-s[ni][nj])
    print(f'#{case} {sums}')

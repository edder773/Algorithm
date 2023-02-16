T = int(input())


def maxs(n):
    t = n[0]
    for x in range(len(n)):
        if t < n[x]:
            t = n[x]
    return t


for case in range(1, T+1):
    N, M = map(int, input().split())
    s = [0]*N
    for i in range(N):
        s[i] = list(map(int, input().split()))

    di = [0, 0, -1, 1]
    dj = [-1, 1, 0, 0]
    temp = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            for t in range(1, s[i][j]+1):
                for k in range(4):
                    ni, nj = i+di[k]*t, j+dj[k]*t
                    if 0 <= ni < N and 0 <= nj < M:
                        temp[i][j] += s[ni][nj]
    temp1 = []
    for x in range(N):
        for y in range(M):
            temp1.append(temp[x][y]+s[x][y])
    print(f'#{case} {maxs(temp1)}')

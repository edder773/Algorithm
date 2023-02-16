N, M = map(int, input().split())
S = []


def dfs(m):
    if len(S) == M:
        print(' '.join(map(str, S)))
        return

    for i in range(m, N+1):
        S.append(i)
        dfs(i)
        S.pop()


dfs(1)

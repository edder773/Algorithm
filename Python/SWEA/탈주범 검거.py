def direction(n): # 방향 정해주기
    if n == 1:
        return [[1, 0], [-1, 0], [0, 1], [0, -1]]
    elif n == 2:
        return [[1, 0], [-1, 0]]
    elif n == 3:
        return [[0, 1], [0, -1]]
    elif n == 4:
        return [[-1, 0], [0, 1]]
    elif n == 5:
        return [[1, 0], [0, 1]]
    elif n == 6:
        return [[1, 0], [0, -1]]
    elif n == 7:
        return [[-1,0], [0, -1]]

def bfs(a,b): # bfs 탐색
    visited = [[0]*M for _ in range(N)]
    queue = [[a,b]]
    visited[a][b] = 1
    cnt = 0
    while queue:
        y, x = queue.pop(0)
        for dy, dx in direction(pipe[y][x]):
            ny, nx = y + dy, x + dx
            # 밖으로 나가지않고, pipe가 지나갈 수 있는 범위에서 방문하지 않았을 경우
            if 0 <= ny < N and 0 <= nx < M and pipe[ny][nx] != 0 and visited[ny][nx] == 0:
                if [-dy, -dx] in direction(pipe[ny][nx]): # 이동할 방향이랑 파이프가 이어져있을 경우
                    visited[ny][nx] = visited[y][x]+1
                    queue.append([ny,nx])

    for t in range(N):
        for s in range(M):
            if 0 < (visited[t][s]) <= L:
                cnt += 1
    return cnt

T = int(input())
for case in range(1,T+1):
    N, M, R, C, L = map(int, input().split())
    pipe = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{case} {bfs(R,C)}')
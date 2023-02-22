move = [[1, 0], [-1, 0], [0, 1], [0, -1]]

T = int(input())
for case in range(1, T+1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]
    room_min = 0
    go = 0

    for i in range(N):
        for j in range(N):
            visited = 0
            queue = [[i, j, 0]]
            while queue:
                y, x, temp = queue.pop(0)  # visited >> 횟수
                visited = max(temp, visited)
                for dy, dx in move:
                    ny, nx = y + dy, x + dx
                    # 범위를 넘지않고, 방의차가 1일 때
                    if 0 <= ny < N and 0 <= nx < N and room[ny][nx] - room[y][x] == 1:
                        queue.append([ny, nx, visited + 1])
            if go < visited:  # 방문거리 최대 찾기
                go = visited
                room_min = room[i][j]
            elif go == visited:
                if room_min > room[i][j]:
                    room_min = room[i][j]
    print(f'#{case} {room_min} {go+1}')

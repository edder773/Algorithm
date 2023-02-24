import sys
N, M = map(int, sys.stdin.readline().split())
r, c, d = map(int ,sys.stdin.readline().split())
room = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

visited = [[0]*M for _ in range(N)] # 방문처리
visited[r][c] = 1 #최초 입력
dr = [-1, 0, 1, 0] # 4방향
dc = [0, 1, 0, -1]
cnt = 1 # 최초 입력시 1번 칠했으니까 1
while True:
    clean = 0 # 청소 할 수 있다 치자
    for _ in range(4) :
        d = (d+3) % 4 # d값에 따라 90도로 돈다 d = 1이면 d = 0이되고 다시 d=3이 되고...
        dy, dx = r + dr[d], c + dc[d]
        if 0 <= dy < N and 0 <= dx < M and room[dy][dx] == 0 and visited[dy][dx] == 0: #청소도 안했고, 방문도 안했으면
                visited[dy][dx] = 1 #방문하고 1로 칠하자
                cnt += 1 # 청소했으니 횟수 +1
                r, c, clean = dy, dx, -1 #이때, 청소 했으니까 거기로 이동하고 청소 이미 끝냈으니 -1 
                break
    if clean == 0: # 청소 할 수 없을 경우
        if room[r-dr[d]][c-dc[d]] == 1: # 청소기 뒤가 1이면
            print(cnt) #청소한 갯수 출력 후 끝
            break
        else :
            r, c = r-dr[d], c-dc[d] #아니면 돌아가기
        
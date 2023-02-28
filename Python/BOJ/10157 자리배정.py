C, R = map(int, input().split())
K = int(input())
dy = [-1, 0, 1, 0] # y 방향
dx = [0, 1, 0, -1] # x 방향
a = [[0]*C for _ in range(R)] # 만들어줄 표 
move = 0 # 움직임 방향
y, x = R-1, 0 #초기 시작 위치
cnt = 0 # K번째 수를 찾기 위해 횟수 count
if K > C*R: # 주어진 K 값이 전체 영역갯수보다 크면
    print(0) # 0 
else :
    for k in range(1,C*R+1):
        a[y][x] = k #초기 시작위치부터 1씩 찍어가면서 움직임
        ny = y + dy[move]
        nx = x + dx[move]
        cnt += 1
        if cnt == K: # 원하는 횟수를 찾앗을 때
            result = [x+1,R-y] # 그때 자리 위치 반환
        if 0 <= ny < R and 0 <= nx < C and a[ny][nx] == 0:
            y,x  = ny, nx
        else :
            move = (move+1)%4
            y, x = y + dy[move], x + dx[move]
    print(*result)
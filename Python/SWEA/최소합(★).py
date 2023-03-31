def find(y,x): # 찾기
    global result, temp # 결과 값과 임시 값
    if result < temp: # 임시 값이 결과 값을 넘어버리면
        return # 끝내

    if x == N-1 and y == N-1: # 목적지에 도착했으면
        result = temp # 결과 값에 임시 값을 반환해
        return

    for dy, dx in move: # 오른쪽 아래쪽 탐색 탐색
        ny, nx = y + dy, x + dx
        if 0 <= ny < N and 0 <= nx < N:
            temp += board[ny][nx] # 값넣어
            find(ny,nx) # 뒤져 보고
            temp -= board[ny][nx] # 아니면 돌아와

T = int(input())
for case in range(1,T+1):
    move = [[1,0],[0,1]]
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    result = float('inf')
    temp = board[0][0] # 0,0 부터시작
    find(0,0)
    print(f'#{case} {result}')
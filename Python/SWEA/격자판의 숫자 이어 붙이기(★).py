def find(y,x,num):
    if len(num) == 7: #길이가 7이야
        result.append(num) # 리스트에 넣자
        return # 끝
    for dy, dx in move : # 움직이자
        ny, nx = y + dy, x + dx
        if 0<= ny < 4 and 0 <= nx < 4: 
            find(ny,nx,num+board[ny][nx]) #번호 붙여가면서 찾아보자

T = int(input())
for case in range(1,T+1): 
    board = [list(input().split()) for _ in range(4)]
    move = [[1,0],[0,1],[-1,0],[0,-1]] # 윰작암
    result = [] # 저장
    for i in range(4): # 시작
        for j in range(4): #위치
            find(i,j,board[i][j]) # 지정
    print(f'#{case} {len(set(result))}')
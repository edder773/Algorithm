def find(a,b,n):
    global result
    result = max(result, n)
    for dy, dx in move:
        ny, nx = a + dy, b + dx
        if 0 <= ny < R and 0 <= nx < C :
            p = ord(board[ny][nx]) - ord('A')
            if not alpha[p]:
                alpha[p] = 1
                find(ny, nx, n+1)
                alpha[p] = 0

import sys
R, C = map(int, sys.stdin.readline().split())
board = list(sys.stdin.readline().strip() for _ in range(R))
move = [[0,1],[1,0],[-1,0],[0,-1]]
alpha = [0]*26 # 알파벳 26자리
start = ord(board[0][0]) - ord('A') # 아스키코드 변환 A:0 B:1 ....
alpha[start] = 1
result = 0
find(0,0,1)
print(result)
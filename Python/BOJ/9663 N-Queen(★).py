def backtracking(k):
    global cnt
    for i in range(N):
        if queen(k,i): # 유망하면
            board[k] = i
            if k == N-1: #다 놓았다면
                cnt += 1
                return
            else:
                backtracking(k+1)
def queen(a,b): #유망 조건
    for i in range(a):
        if board[i] == b or abs(board[i]-b) == abs(i-a): # 같은 열이거나 같은 대각선
            return False 
    return True 

import sys
N = int(sys.stdin.readline())
board = [0]*N 
cnt = 0
backtracking(0)
print(cnt)
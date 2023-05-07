def find(times, score, pin):
    global result
    if times == 10:
        result = max(score, result)
        return 
    for i in range(4):
        x = pin[i]
        if len(board[x]) == 2:
            n = board[x][1]
        else :
            n = board[x][0]
        for _ in range(1, dice[times]):
            n = board[n][0]
        if n == 32 or (n < 32 and n not in pin): 
            temp = pin[i]
            pin[i] = n
            find(times+1, score + board_score[n],pin)
            pin[i] = temp


import sys
dice = list(map(int,sys.stdin.readline().split()))
# 다음 칸에 이동 가능한 그래프를 표현(0번(출발) -> 1, 1번 ->2 ... 5번 -> 6, 21)
board = [[1], [2], [3], [4], [5], [6, 21], [7], [8], [9], [10], [11, 25], [12], [13], [14], [15], [16, 27], [17], [18], [19], [20], [32], [22], [23], [24], [30], [26], [24], [28], [29], [24], [31], [20], [32]]
board_score = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 13, 16, 19, 25, 22, 24, 28, 27, 26, 30, 35, 0]
result = 0

find(0,0,[0,0,0,0])
print(result)
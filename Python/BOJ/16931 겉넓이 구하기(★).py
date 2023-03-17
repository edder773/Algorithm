import sys
N, M = map(int, sys.stdin.readline().split())
square = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] 
side1 = 0 # 왼쪽에서 볼때
side2 = 0 # 오른쪽에서 볼때
side3 = N*M #위나 아래에서 볼때

for i in range(N):
    for j in range(M):
        if j == 0: # 맨 앞면
            side1 += square[i][j] 
        else : #앞면 아니면
            if square[i][j] > square[i][j-1]: #다음 블록이 이전꺼보다 커!
                side1 += square[i][j] - square[i][j-1] # 그럼 차이만큼 더하자

for j in range(M):
    for i in range(N):
        if i == 0: # 맨 앞면
            side2 += square[i][j] 
        else : #앞면 아니면
            if square[i][j] > square[i-1][j]: #다음 블록이 이전꺼보다 커!
                side2 += square[i][j] - square[i-1][j] # 그럼 차이만큼 더하자
print((side1+side2+side3)*2)
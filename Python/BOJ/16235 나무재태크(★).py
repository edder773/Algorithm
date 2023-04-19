# 조건 1. N*N크기의 땅, 가장 처음 양분은 모든 칸에 5
# 조건 2. M개의 나무를 구매해 땅에 심음
# 조건 3. 봄 : 나무가 자신의 나이만큼 양분먹고 나이 +1, 한칸에 여러 나무가 있으면 나이가 어린 나무부터 양분을 먹고 못먹으면 사망
# 조건 4. 여름 : 봄에 죽은 나무의 나이//2 -> 양분
# 조건 5. 가을 : if 나무나이 % 5 == 0 : 인접한 8칸에 나이가 1인 나무 번식
# 조건 6. 겨울 : 땅에 양분 추가

import sys
from collections import deque
N,M,K = map(int, sys.stdin.readline().split())
farm = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
tree = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
small_tree = [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]
fertilizer = [[5]*N for _ in range(N)] # 조건 1
land = [[deque() for _ in range(N)] for _ in range(N)]
result = 0
while tree: # 최초 나무 심기
    r, c, age = tree.pop()
    land[r-1][c-1].append(age)

for _ in range(K): # K 년동안
    for i in range(N):
        for j in range(N):
            for k in range(len(land[i][j])):
                if fertilizer[i][j] >= land[i][j][k]: # 비료가 남아있으면
                    fertilizer[i][j] -= land[i][j][k] # 나무가 나이만큼 비료를 먹고
                    land[i][j][k] += 1 # 나무 나이 증가
                else : # 조건 4
                    for _ in range(k,len(land[i][j])): # 안남았단건 다 죽여야하니
                        x = land[i][j].pop()
                        fertilizer[i][j] += x//2 # 죽은 나무의 양분
                    break
                
    for i in range(N):
        for j in range(N):
            for k in range(len(land[i][j])): # 조건 5
                if land[i][j][k] % 5 == 0 :
                    for dy, dx in small_tree:
                        ny, nx = i + dy, j + dx
                        if 0 <= ny < N and 0 <= nx < N: # 범위 안벗어나면
                            land[ny][nx].appendleft(1) # 1살짜리 나무 친구들 생성
                
    for i in range(N): # 조건 6 #겨울 지나면
        for j in range(N):
            fertilizer[i][j] += farm[i][j] # 비료 증가

for i in range(N):
    for j in range(N):
        result += len(land[i][j])
print(result)
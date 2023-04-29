# 조건 1 : 경사로를 놓아서 지나가는 길을 만들 수 있음
# 조건 2 : 경사로는 높이가 항상 1이고 길이는 L
# 조건 3-1 : 경사로는 낮은칸에 놓이고, L개의 연손된 칸에 경사로 바닥이 모두 접해야함
# 조건 3-2 : 낮은 칸과 높은 칸의 높이 차이는 1
# 조건 3-3 : 경사로를 놓을 낮은 칸의 높이는 모두 같아야하며 L개의 칸이 연속적
# 조건 4-1 : 경사로를 놓인곳에 또놓으면 x
# 조건 4-2 : 경사로 범위를 벗어나면 안됨
# 조건 4-3 : 낮은 곳의 높이가 모두 같지 않은 경우
def find(ways):
    visited = [False]*N
    for i in range(1,N):
        if abs(ways[i] - ways[i-1]) > 1: # 조건 2
            return False
        if ways[i-1] > ways[i] : # 낮은 지점이 더 클 때
            for j in range(L): # 경사로 크기까지
                if i + j >= N or ways[i] != ways[i+j] or visited[i+j]: # 경사로가 밖을 벗어나거나, 길이가 다르거나, 이미 설치했다면 (조건 4)
                    return False
                if ways[i] == ways[i+j]: # 좌우 높이가 같으면 (조건 1) 
                    visited[i+j] = True # 경사로 놓자 
        elif ways[i-1] < ways[i] : # 높은 지점이 더 클 때
            for j in range(L):
                if i - j - 1 < 0 or ways[i-1] != ways[i - j - 1] or visited[i - j - 1]: # 경사로가 밖을 벗어나거나, 길이가 다르거나, 이미 설치했다면 (조건 4)
                    return False
                if ways[i-1] == ways[i-j-1]: #조건 1
                    visited[i-j-1] = True
    return True

import sys
N, L = map(int, sys.stdin.readline().split())
way = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
cross = list(zip(*way))
result = 0
for i in range(N) :
    if find(way[i]):
        result += 1
    if find(cross[i]):
        result += 1
print(result)
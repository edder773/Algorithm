# 조건
# 위에서부터 r행, c열 // 단 r과 c는 1부터
# 치킨거리는 집을 기준으로 정해지고 가장 가까운 치킨집과의 거리
# 도시의 치킨 거리는 모든 치킨거리의 합 -> 구해야할 것
# 두 칸 사이의 거리는 |r1-r2|+|c1-c2|
def close(a,b): # 요구사항인 M개 만큼 치킨집을 폐업해보자
    global distance_min
    if a > len(chicken):
        return
    if b == M:
        distance_all = 0
        for r, c in house:
            distance = float('inf')
            for i in val:
                rr, cc = chicken[i]
                distance = min(distance, abs(rr-r)+abs(cc-c))
            distance_all += distance
        distance_min = min(distance_min, distance_all)
        return

    val.append(a)
    close(a+1, b+1)
    val.pop()
    close(a+1,b)

import sys
N, M = map(int, sys.stdin.readline().split())
city = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
chicken, house, val = [], [], []

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            house.append([i,j])
        elif city[i][j] == 2:
            chicken.append([i,j])

distance_min = float('inf')
close(0,0)
print(distance_min)
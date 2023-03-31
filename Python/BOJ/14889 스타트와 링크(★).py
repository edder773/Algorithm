def team(a,n):
    global result
    if a == N//2: # 유망하다면
        start, link = 0, 0 # start 팀, link팀
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]: # 만약 i, j 둘다 방문한거라면
                    start += S[i][j] # 스타트팀에 배정
                elif not visited[i] and not visited[j]: # i,j 둘다 방문 안했으면
                    link +=S[i][j] # 링크 팀에 배정
        result = min(result,abs(start-link)) # 최소값
        return
    else :
        for x in range(n,N): 
            if visited[x] == 0: # 방문 안했으면
                visited[x] = 1 # 방문 체크
                team(a+1,x+1) # 횟수 늘려
                visited[x] = 0 # 되돌아가
import sys
N = int(sys.stdin.readline())
S = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [0]*N
result = float('inf')
team(0,0)
print(result)

# # 특수케이스
# import sys
# from itertools import combinations
# N = int(sys.stdin.readline())
# stat = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# sum_stat = [sum(i) + sum(j) for i, j in zip(stat, zip(*stat))] # 대각선끼리 합
# allstat = sum(sum_stat) // 2 # 모든 값 합의 절반
# result = float('inf')
# for l in combinations(sum_stat, N//2): # 대각선 합에서 뽑은 2개 중에서
#     result = min(result, abs(allstat - sum(l))) # 모든 값의 절반 - 그 뽑은 2개 합의 차 = start팀 - link팀
# print(result) 
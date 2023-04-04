import sys
N = int(sys.stdin.readline())
h = list(map(int, sys.stdin.readline().split()))
rank = [0]*N
for i in range(N):
    cnt = 0
    for j in range(N):
        if rank[j] == 0: # 아직 비었고
            if cnt == h[i]: # 그떄 카운트가 h[i]와 일치하면
                rank[j] = i+1 # 넣고
                break # 지금 탐색 끝
            else : # 일치하지 않으면
                cnt += 1 # 키 증가
print(*rank)
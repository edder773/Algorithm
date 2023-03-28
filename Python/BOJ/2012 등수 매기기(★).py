import sys
N = int(sys.stdin.readline())
rank = sorted([int(sys.stdin.readline()) for _ in range(N)]) # 정렬해서 받기
cnt = 0 
for i in range(N):
    if rank[i] != i+1: # 자기 예상 등수와 실제 등수가 다르면
        cnt += abs(rank[i]-(i+1)) # 둘의 차이만큼 cnt에 더하기
print(cnt)
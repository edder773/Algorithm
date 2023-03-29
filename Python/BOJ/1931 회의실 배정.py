import sys
N = int(sys.stdin.readline())
# 1번 인덱스를 기준으로 정렬
meeting = sorted([list(map(int,sys.stdin.readline().split())) for _ in range(N)], key=lambda x:(x[1],x[0]))
cnt = 1 # 가능 횟수 체크
temp = meeting[0][1] # 맨 앞시작 값
for i in range(1,N):
    if meeting[i][0] >= temp: # 시작시간이 현재 끝나는 시간보다 크면
        temp = meeting[i][1] # 끝나는 시간 저장하고
        cnt += 1 #횟수 증가
print(cnt)
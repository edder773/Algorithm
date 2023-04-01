# 조건 0 : 격자 행과 열은 1~N까지 번호로 되어있고, 각각 이어져있음
# -> 1~N = 1~N + 1~N + 1~N 이런형태
# 조건 1 : 파이어볼이 자신의 방향 d로 속력 s칸만큼이동
# 조건 2 : 이동 끝나면 2개이상 있으면 특수효과 발생
# 조건 2-1 : 파이어볼 합쳐짐
# 조건 2-2 : 파이어볼 4개로 나뉘어짐
# 조건 2-3 : 나뉘어지면 질량 = sum(질량)/5, 속력 = sum(속력)/갯수 , 방향 홀수거나 짝수면 0,2,4,6 else 1,3,5,7
# 조건 2-4 : 질량 0 이면 사라짐

import sys
from collections import deque
N, M, K = map(int,sys.stdin.readline().split())
board = deque(deque(deque()*N for _ in range(N)) for _ in range(N)) # 칸 마다 들어갈거 지정해줘야하니 3중
dx = [-1, -1, 0, 1, 1, 1, 0, -1] # 파이어볼 방향
dy = [0, 1, 1, 1, 0, -1, -1, -1]
fireball = deque()
for _ in range(M):
    r, c, m, s, d = map(int, sys.stdin.readline().split())
    fireball.append([r-1,c-1,m,s,d]) # 시작 인덱스 맞춰주기

for _ in range(K):
    while fireball:
        r, c, m, s, d = fireball.popleft()
        nr, nc = (r+ s* dx[d]) % N, (c + s* dy[d]) % N # 조건 0번, 조건 1번
        board[nr][nc].append([m,s,d]) # 해당 칸에 m,s,d 기록

    for y in range(N):
        for x in range(N):
            if len(board[y][x]) > 1: # 해당 칸에 파이어볼이 2개 이상인 경우 조건 2
                # 질량합, 속력합, 방향이 모두 짝수 or 홀수인지 체크 , 합쳐진 파이어볼 갯수
                m_sum, s_sum, d_odd, d_even, cnt = 0, 0, 0, 0, len(board[y][x]) #조건 2-1
                while board[y][x]:
                    m, s, d = board[y][x].popleft()
                    m_sum += m
                    s_sum += s
                    if d % 2 == 0:
                        d_even += 1
                    else :
                        d_odd += 1

                if d_even == cnt or d_odd == cnt: #조건 2-3
                    mini_ball = [0,2,4,6] #조건 2-2
                else:
                    mini_ball = [1,3,5,7]

                if m_sum//5 > 0: # 조건 2-4
                    for d in mini_ball:
                        fireball.append([y, x, m_sum//5, s_sum//cnt, d])

            elif len(board[y][x]) == 1:
                m, s, d = board[y][x].pop()
                fireball.append([y, x, m, s, d])

result = 0
for i in fireball: # 질량 합 구하기
    result += i[2]
print(result)
import sys
from collections import deque
T = int(sys.stdin.readline())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    impo = deque(map(int, sys.stdin.readline().split())) # 문서 순서
    cnt = 0
    while impo:
        out = max(impo) # 우선순위가 가장 높은게 나가므로
        front = impo.popleft() #맨 앞에 있는걸 꺼냄
        M -= 1 # 찾고자하는 것의 위치 -1

        if out == front: #우선순위 가장높은거 = 맨앞에 있으면
            cnt += 1 # 출력 +1
            if M <0: # M <0 이면 가장 앞에 있는거므로
                print(cnt) # 그때 cnt 출력
                break # 끝
        else: #아니면
            impo.append(front) #다시 뒤로 붙여
            if M < 0: # 이때 찾는게 맨앞에 있으면
                M = len(impo)-1 # 맨 뒤의 위치 지정
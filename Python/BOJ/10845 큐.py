import sys
from collections import deque

N = int(sys.stdin.readline())
queue = deque()
for _ in range(N):
    A = sys.stdin.readline().split()
    if A[0] == 'push': # push일 경우
        queue.append(A[1]) #정수 삽입

    elif A[0] == 'pop': #pop일 경우
        if len(queue) == 0: #비었으면
            print(-1) # -1출력
        else :
            print(queue.popleft()) #아니면 왼쪽꺼 빼기

    elif A[0] == 'size': #size일 경우
        print(len(queue)) #길이 출력

    elif A[0] == 'empty': #empty일 경우
        if len(queue) == 0: #비었으면
            print(1) # 1출력
        else :
            print(0) #아님 0

    elif A[0] == 'front': #front일 경우
        if len(queue) == 0 : #비었으면
            print(-1) # -1출력
        else:
            print(queue[0]) #아니면 맨앞에꺼 출력

    elif A[0] == 'back': # back일경우
        if len(queue) == 0: #비었으면
            print(-1) # -1출력
        else:
            print(queue[-1]) #아니면 맨 뒤에꺼 출력
import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
queue = list(map(int, sys.stdin.readline().split()))
nums = deque(i for i in range(1,N+1))

cnt = 0
for i in queue: #입력 값들에 대해
    while True:
        if nums[0] == i: # 입력과 num[0]이 같으면 
            nums.popleft() # 뽑고 
            break #끝
        else:
            if nums.index(i) <= len(nums)//2: #i에 해당하는 num의 인덱스가 전체 길이보다 작거나 같으면
                # 즉 오른쪽에 있으면
                nums.rotate(-1) #2번 연산
                cnt += 1 #횟수 측정
            else:
                nums.rotate(1) #왼쪽에 있으면 3번 연산
                cnt += 1 #횟수 측정
print(cnt)
def check(now, after):
    before, cnt = now.copy(), 0
    for i in range(1,N):
        if before[i-1] != after[i-1]: #해당 전구 번호 다르면
            cnt += 1 # 누르고
            for j in range(i-1, i+2):
                if j < N: # 마지막 스위치는 i-1 까지만 존재
                    before[j] = 1 - before[j] # 바꿔주기

    if before == after: #같으면
        return cnt # 횟수 반환
    else:
        return float('inf')

import sys, copy
N = int(sys.stdin.readline())
now = list(map(int,sys.stdin.readline().strip()))
make = list(map(int,sys.stdin.readline().strip()))
result = check(now, make)
now[0], now[1] = 1 - now[0], 1 - now[1] # 처음꺼 바꿔주고
result = min(result, check(now,make) + 1) # 다시 체크
if result == float('inf'):
    print(-1)
else :
    print(result)
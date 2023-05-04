import sys
from itertools import product
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
button = [i for i in range(10)]
if M: # 고장난게 있으면 받음
    broken = list(map(int, sys.stdin.readline().split()))
    for i in broken: #고장난 버튼 제외
        button.remove(i)
        
now,nows,nowss = 100, 100, 100 # 현재 위치 x3
result1,result2, result3, = 0, 0, 0 # 최종 버튼 누른 횟수
near,nears,nearss = 5000000, 5000000, 5000000 # 숫자로 갔을 때 가까운 값과 N의 차이
if now == N :# 이미 그 채널이면
    print(0) # 끝
else : 
    check = 0 # 숫자 없이 직접 + -만 눌렀을 경우
    while now != N:
        if N - now > 0:
            now += 1
        elif N - now < 0:
            now -= 1
        check += 1
        
    if len(str(N))-1 > 0: # N의 자리수보다 한자릿수 작은 숫자들 집합
        for i in product(button,repeat = len(str(N))-1):
            temp = ''
            for j in i:
                temp += str(j)
            temp = int(temp)
            if abs(N - temp) <= near:
                nearss = abs(N-temp)
                nowss = temp
        result3 += nearss + len(str(nowss))
    else : 
        result3 = 500000
        
    for i in product(button,repeat = len(str(N))): # N의 자릿수와 같은 숫자들의 집합
        temp = ''
        for j in i:
            temp += str(j)
        temp = int(temp)
        if abs(N - temp) <= near:
            near = abs(N-temp)
            now = temp
    result1 += near + len(str(now))
    
    for i in product(button,repeat = len(str(N))+1): # N의 자리수보다 한자릿수 더 큰 숫자들의 집합
        if i[0] > 1:
            break
        temp = ''
        for j in i:
            temp += str(j)
        temp = int(temp)
        if abs(N - temp) <= nears:
            nears = abs(N-temp)
            nows = temp
    result2 += nears + len(str(nows))
    print(min(result1, result2, result3, check))
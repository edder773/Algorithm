def check(n):
    num = 0
    for i in range(1, int(n**0.5)+1): # 에라토스테네스의 체 응용
        num += x[i] * (n // i**2) 
    return num

def bin_search(): # 이진 탐색을 통한 숫자 찾기
    left, right = 0, 2000000000
    while left  <  right-1:
        mid = (left + right) // 2
        if check(mid) < K:
            left = mid
        else:
            right = mid
    return right

import sys
K = int(sys.stdin.readline())
# 뫼비우스 함수 
x = [0] * 42000 
x[1] = 1
for i in range(1, 42000): 
    for j in range(i*2,42000,i):
        x[j] -= x[i] 

print(bin_search())
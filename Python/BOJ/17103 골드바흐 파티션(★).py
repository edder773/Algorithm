def prime(n): #에라토스테네스의 체로 소수 리스트 뽑기
    array = [False]*2 + [True]*n
    m = int(n**0.5)
    for i in range(2,m+1):
        if array[i] == True:
            for j in range(i*i,n,i):
                array[j] = False
    return array

primes = prime(1000000)

import sys
T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    cnt = 0
    for i in range(N//2+1): # 대칭기준 같으면 제외
        if primes[i] and primes[N-i]:
            cnt += 1
    print(cnt)
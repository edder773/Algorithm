def Lucas(n,k): #뤼카의 정리
    if n < k : # nCk 에서 K가 더 클 경우
        return 0
    elif n == k : # nCk 에서 n과 k가 같을 경우
        return 1 
    x = 1
    for i in range(1, k+1): # 그외 k가 더 큰 경우 k까지 늘려가면서 
        x *= n - i + 1 # 곱해주고
        x //= i # 나눠주자
    return x
        

import sys
N, K, M = map(int, sys.stdin.readline().split())
n, m = [], []
cnt = 0
while N or K : # 둘중 0이 될 때 까지
    n.append(N%M) #소수로 나눈 나머지 기록
    m.append(K%M) #소수로 나눈 나머지 기록
    N //= M
    K //= M
print(n,m)   
result = 1
for i in range(len(n)):
    result *= Lucas(n[i],m[i]) #뤼카의 정리를 이용한 계산
    result %= M
print(result)
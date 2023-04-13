from itertools import combinations
import sys
# N에 대한 소수 집합 구해주기 (N과 서로소 체크)
def prime(n): # 소수 구하기 
    result = [] # 소수 집합
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            result.append(i)
            while n % i == 0: # n이 매우 크니 나눠주기
                n //= i
    if n > 1: # n도 포함되어야 하므로
        result.append(n) # 넣어주기
    return result

T = int(sys.stdin.readline())
for case in range(1, T+1):
    A, B, N = map(int, sys.stdin.readline().split())
    x, result_A, result_B = prime(N), A-1, B
    for i in range(1, len(x)+1): 
        for comb in combinations(x,i): # 소수 조합에 대해서
            m = 1 # 포함 배제의 원리를 위한 나누기용 (아래는 포함 배제 원리)
            for j in comb:
                m *= j
            if i % 2 :
                result_A -= (A-1)//m
                result_B -= B//m
            else :
                result_A += (A-1)//m
                result_B += B//m
    
    print(f'Case #{case}: {result_B-result_A}')
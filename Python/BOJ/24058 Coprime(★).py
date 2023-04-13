def primt(n): # 소수 구하기
    result = []
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            result.append(i)
            while n % i == 0:
                n //= i
    if n > 1:
        result.append(n)
    return result

from itertools import combinations
import sys
n, k = map(int, sys.stdin.readline().split())
m, result = n*k, n*k 
x = primt(n)
for i in range(1,len(x)+1):
    for comb in combinations(x,i): # 소수 조합에 대해서
        div = 1
        # 포함 배제의 원리로 서로수의 개수 구하기
        for j in comb:
            div *= j
        if i % 2 :
            result -= m//div
        else:
            result += m//div
if n == 1: # n == 1이면 그냥 모든 수의 합
    print(m*(m+1)//2)
else :
    print(result*m//2) # 서로수의 합 = 서로수의 개수 * 구하고자한 수 //2
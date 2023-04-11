def find(a):
    global num, result
    if a == N :
        if not num : # 비었으면
            return # 끝
        
        temp = 1
        for i in range(len(num)): # 각 부분 집합의 곱
            temp *= num[i]
        
        #포함 배제의 원리
        if len(num) % 2 : # 홀수면
            result += M // temp # 더하고
        else : # 짝수면
            result -= M // temp # 빼고
        return
    
    num.append(x[a])
    find(a+1)
    num.pop()
    find(a+1)
    
import sys
N, M = map(int, sys.stdin.readline().split())
x = list(map(int, input().split()))
num = []
result = 0
find(0)
print(result)
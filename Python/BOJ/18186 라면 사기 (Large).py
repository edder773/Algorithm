def buy1(n): # 1개 살 경우
    global result
    result += B * x[n]

def buy2(n): # 2개 살 경우
    global result
    m = min(x[n:n+2])
    x[n] -= m
    x[n+1] -= m
    result += (B+C)* m    

def buy3(n): # 3개 살 경우
    global result
    m = min(x[n:n+3])
    x[n] -= m
    x[n+1] -= m
    x[n+2] -= m
    result += (B+2*C)* m


import sys
N, B, C = map(int, sys.stdin.readline().split())
x = list(map(int, sys.stdin.readline().split())) + [0,0]
if C > B : # C 가 B보다 크면 
    C = B # 걍 B로 사는게 이득 (buy1, buy2,buy3 가격 B, 2B, 3B가 되게)
result = 0
for i in range(N):
    if x[i+1] > x[i+2]:
        m = min(x[i], x[i+1] - x[i+2]) 
        x[i] -= m
        x[i+1] -= m
        result += (B+C)*m 
        buy3(i) 
        buy1(i) 
    else :
        buy3(i)
        buy2(i)
        buy1(i)
print(result)
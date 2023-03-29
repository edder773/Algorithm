def mult(a,b):
    A = [[0,0],[0,0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                A[i][j] += a[i][k]*b[k][j] % 1000
    return A

def div(x,n):
    if n == 1:
        return x
    else :
        temp = div(x,n//2)
        if n % 2 == 0:
            return mult(temp,temp) 
        else:
            return mult(mult(temp,temp),x)


import sys, math
T = int(sys.stdin.readline())
for case in range(1,T+1):
    N = int(sys.stdin.readline())
    x = [[6,-4],[1,0]]
    result = div(x,N)
    num = str((result[0][0] + result[1][1] -1)%1000)
    if len(num) == 3:
        print(f'Case #{case}: {num}')
    elif len(num) == 2:
        print(f'Case #{case}: 0{num}')
    elif len(num) == 1:
        print(f'Case #{case}: 00{num}')
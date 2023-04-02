def factorial(n):
    result = 1
    while n:
        result = (result * n) %p
        n -= 1
    return result

def find(x,n):
    if n == 1:
        return x % p
    else :
        temp = find(x,n//2)
        if n % 2 == 0:
            return temp*temp % p
        else:
            return temp*temp*x % p

import sys
N, R, M = map(int, sys.stdin.readline().split())
p = M
print(factorial(N)%p*find(factorial(R)*(factorial(N-R)%p),p-2)%p)
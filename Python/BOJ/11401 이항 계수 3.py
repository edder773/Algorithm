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
N, R = map(int, sys.stdin.readline().split())
p = 1000000007
print(factorial(N)*find(factorial(R)*(factorial(N-R)),p-2)%p)
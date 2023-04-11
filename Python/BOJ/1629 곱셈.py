def find(x,n):
    if n == 1:
        return x
    temp = find(x,n//2)
    if n % 2 == 0:
        return temp*temp % C
    else : 
        return temp*temp*x % C

import sys
A, B, C = map(int, sys.stdin.readline().split())
print(find(A,B)%C)
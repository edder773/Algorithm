import sys
from math import gcd
A, B = map(int, sys.stdin.readline().split())
C, D = map(int, sys.stdin.readline().split())
numerator = A*D + B*C
denominator = B*D
GCD = gcd(numerator,denominator)
print(numerator/GCD, denominator/GCD)
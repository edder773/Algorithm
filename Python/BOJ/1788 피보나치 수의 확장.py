import sys
n = int(sys.stdin.readline())
F = [0]*(1000001)
p = 1000000000
F[1] = 1
for i in range(2,1000001):
    F[i] = (F[i-1] + F[i-2]) % p

if n % 2 == 0 and n < 0:
    print(-1)
elif n == 0:
    print(0)
else:
    print(1)
print(F[abs(n)])
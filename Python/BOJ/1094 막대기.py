import sys
X = int(sys.stdin.readline())
num = 64
result = 0
while num:
    a = X // num
    result += a
    X -= num * a
    num //= 2
print(result)
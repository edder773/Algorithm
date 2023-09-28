import sys
N, X = map(int, sys.stdin.readline().split())
blog = list(map(int, sys.stdin.readline().split()))
if max(blog) == 0:
    print('SAD')
else:
    x = sum(blog[:X])
    value = x
    result = 1
    for i in range(X, N):
        value -= blog[i-X]
        value += blog[i]
        if value > x:
            x = value
            result = 1
        elif value == x:
            result += 1
    print(x)
    print(result)

import sys
T = int(sys.stdin.readline())
for _ in range(T):
    X, Y = map(int, sys.stdin.readline().split())
    num = [2**i for i in range(33)]
    a = Y-X
    if a == 0 :
        print(0)
    else:
        n = int((Y-X)**0.5)
        if n**2 == a:
            print(2*n-1)
        else:
            if a-n**2 <= n:
                print(2*n)
            else:
                print(2*n+1)
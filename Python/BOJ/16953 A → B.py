import sys
A, B = map(int, sys.stdin.readline().split())
cnt = 1
while True:
    if A == B:
        print(cnt)
        break
    elif (B % 10 != 1 and B % 2 != 0) or (B < A):
        print(-1)
        break
    else :
        if B % 10 == 1:
            B //= 10
            cnt += 1
        else : 
            B //= 2
            cnt += 1
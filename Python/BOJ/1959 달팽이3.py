import sys
M, N = map(int, sys.stdin.readline().split())

if M > N:
    print((N-1)*2 + 1)
else :
    print((M-1)*2)

if M == N:
    if M % 2:
        print(M // 2 + 1, N//2 + 1)
    else :
        print(M // 2 + 1, N//2)
elif M > N:
    if N % 2 :
        print(N // 2 + 1 + M - N, N // 2 +1 )
    else:
        print(N // 2 + 1, N // 2)
else : 
    if M % 2:
        print(M // 2 + 1, M // 2 + 1 + N - M)
    else :
        print(M // 2 + 1, M // 2)
T = int(input())
for case in range(1, T+1):
    x = list(map(str, input().split()))
    A = list(x[0])
    B = list(x[1])
    for i in range(len(A)):
        if A[i:i+len(B)] == B:
            A[i:i+len(B)] = 'O'
    print(f'#{case} {len(A)}')

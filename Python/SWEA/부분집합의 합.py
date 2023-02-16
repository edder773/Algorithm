def sums(n):
    k = 0
    for i in n:
        k += i
    return k


T = int(input())
for case in range(1, T+1):
    N, K = map(int, input().split())
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    cnt = 0
    for i in range(1 << len(A)):
        e = []
        for j in range(len(A)):
            if i & (1 << j):
                e += [A[j]]

        if len(e) == N:
            if sums(e) == K:
                cnt += 1
    print(f'#{case} {cnt}')

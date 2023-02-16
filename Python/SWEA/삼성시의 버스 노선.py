T = int(input())
for case in range(1, T+1):
    base = [0]*5001
    N = int(input())
    s = [0]*N
    for i in range(N):
        A, B = map(int, input().split())
        s[i] = [t for t in range(A, B+1)]
    P = int(input())
    C = [0] * P
    for j in range(P):
        C[j] = int(input())
    for x in range(len(s)):
        for y in range(len(s[x])):
            base[s[x][y]] += 1
    T = [0]*P
    print(f'#{case}', end=' ')
    for z in range(len(C)):
        T[z] = base[C[z]]
    print(*T)

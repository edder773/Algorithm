T = int(input())
for case in range(1,T+1):
    N, M, L = map(int, input().split())
    tree = [0 for _ in range(N+1)]
    x = [list(map(int, input().split())) for _ in range(M)]
    for a, b in x :
        tree[a] = b

    for i in range(N, 0, -1): # 자식노드부터 더해온다
        if i//2 > 0: 
            tree[i//2] += tree[i]

    print(f'#{case} {tree[L]}') 
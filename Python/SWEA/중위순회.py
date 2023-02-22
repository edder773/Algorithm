def binary(a):
    if a <= N:
        binary(a*2)
        print(tree[a],end='')
        binary(a*2 + 1)


for case in range(1, 11):
    N = int(input())
    tree = [0] * (N + 1)
    for _ in range(N):
        idx, a, *c = input().split()
        tree[int(idx)] = a
    print(f'#{case}','',end='')
    binary(1)
    print()
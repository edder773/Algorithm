def order(i):
    global cnt
    if i == 0:
        return
    cnt += 1
    order(left[i])        # 왼쪽 자식으로 이동
    order(right[i])       # 오른쪽 자식으로 이동

T = int(input())
for case in range(1,T+1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 0
    V = E + 1
    left = [0] * (V+1)
    right = [0] * (V+1)

    for i in range(E):
        p, c = arr[i*2], arr[i*2+1]
        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c
    order(N)
    print(f'#{case} {cnt}')

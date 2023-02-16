def my_abs(n):
    if n > 0:
        return n
    elif n < 0:
        return -n


def sorts(n, k):  # 오름차순 반환
    for i in range(k):
        minindex = i
        for j in range(i+1, len(n)):
            if n[minindex] > n[j]:
                minindex = j
        n[i], n[minindex] = n[minindex], n[i]
    return n[k-1]


T = int(input())
for case in range(1, T+1):
    N = int(input())
    x = list(map(int, input().split()))
    y = x[:]
    sorts(y, N)
    min_x = y[0]
    max_x = y[len(x)-1]

    for i in range(N):
        if x[i] == min_x:
            m = i
            break
    for j in range(N):
        if x[N-1-j] == max_x:
            n = N-1-j
            break
    print(f'#{case} {my_abs(n-m)}')

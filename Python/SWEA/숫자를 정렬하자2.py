def select_low(n, k):  # 오름차순 반환
    for i in range(0, k):
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
    select_low(x, N)
    print(f'#{case}', *x)

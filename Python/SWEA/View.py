def min_h(n):
    cnt = n[0]
    for value in range(len(n)):
        if cnt > n[value]:
            cnt = n[value]
    return cnt


for case in range(1, 11):
    N = int(input())
    h = list(map(int, input().split()))
    sums = 0
    for i in range(2, N-2):
        a1 = h[i] - h[i-2]
        a2 = h[i] - h[i-1]
        a3 = h[i] - h[i+1]
        a4 = h[i] - h[i+2]
        temp = [a1, a2, a3, a4]
        if a1 > 0 and a2 > 0 and a3 > 0 and a4 > 0:
            sums += min_h(temp)
    print(f'#{case} {sums}')

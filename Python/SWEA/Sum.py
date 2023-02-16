def sums(m):
    k = 0
    for num in m:
        k += num
    return k


def maxs(m):
    t = m[0]
    for nums in m:
        if t < nums:
            t = nums
    return t


for case in range(1, 11):
    T = int(input())
    n = [0 for _ in range(100)]
    for x in range(100):
        n[x] = list(map(int, input().split()))
    temp = []
    cross1 = []
    cross2 = []
    all = []
    for i in range(100):
        temp1 = []
        temp.append(sums(n[i]))  # 가로 합
        for j in range(100):
            temp1.append(n[j][i])  # 세로합
        temp.append(sums(temp1))

    for cross in range(100):
        cross1.append(n[cross][cross])  # 좌위 우아
        cross2.append(n[cross][99-cross])  # 우위 좌아

    all.append(maxs(temp))
    all.append(sums(cross1))
    all.append(sums(cross2))
    print(f'#{case} {maxs(all)}')

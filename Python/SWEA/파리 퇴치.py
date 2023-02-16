T = int(input())


def sums(n):
    k = 0
    for num in n:
        k += num
    return k


def maxs(n):
    t = n[0]
    for nums in n:
        if t < nums:
            t = nums
    return t


for case in range(1, T+1):
    N, M = map(int, input().split())
    s = [0]*N
    for x in range(N):
        s[x] = list(map(int, input().split()))
    temp = []
    temp1 = []
    for i in range(N-1):
        for j in range(N-1):
            temp = []
            for k in range(M):
                if i+k < N:
                    temp += s[i+k][j:j+M]
            temp1 += [temp]
    all = []
    # print(temp)
    for x in range(len(temp1)):
        all.append(sums(temp1[x]))
    print(f'#{case} {maxs(all)}')

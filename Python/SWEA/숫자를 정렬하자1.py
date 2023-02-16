def max_n(n):
    num = 0
    for i in range(len(n)):
        if num < n[i]:
            num = n[i]
    return num


def sorting(m):
    temp = [0]*(max_n(m)+1)
    sort_m = []
    for i in m:
        temp[i] += 1
    for j in range(max_n(m)+1):
        for _ in range(temp[j]):
            sort_m += [j]
    return sort_m


#
T = int(input())
for case in range(1, T+1):
    N = int(input())
    l = list(map(int, input().split()))
    print(f'#{case}', *sorting(l))

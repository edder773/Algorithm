import sys


def search(x):  # Parametric Search
    start = 1
    end = max(x)-min(x)  # 최대와 최소의 차
    result = 0
    while start <= end:
        middle = (start + end) // 2
        num = x[0]  # 최소로 지정
        count = 1

        for i in range(1, N):
            if x[i] >= num + middle:  # 최소 + middle보다 크면
                count += 1  # 공유기 갯수 증가
                num = x[i]

        if count >= C:
            start = middle + 1
            result = middle
        else:
            end = middle - 1
    return (result)


N, C = map(int, sys.stdin.readline().split())
x = [0]*N
for i in range(N):
    x[i] = int(sys.stdin.readline())
x.sort()
print(search(x))

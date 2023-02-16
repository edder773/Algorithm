N = int(input())
x = list(input().split())
M = int(input())
y = list(input().split())


def search(a, key):  # 이진 탐색
    start = 0
    end = N-1
    while start <= end:
        middle = (start + end) // 2
        if a[middle] == key:
            return 1
        elif a[middle] > key:
            end = middle - 1
        else:
            start = middle + 1
    return 0


x.sort()  # x정렬 (이진탐색 필수)
for i in y:
    print(search(x, i))

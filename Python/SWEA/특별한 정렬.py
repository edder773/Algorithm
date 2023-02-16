def select_low(n, k):  # k번쨰 최솟값 반환 함수
    for i in range(0, k):
        minindex = i
        for j in range(i+1, len(n)):
            if n[minindex] > n[j]:
                minindex = j
        n[i], n[minindex] = n[minindex], n[i]
    return n[k-1]


def select_high(n, k):  # k번째 최대값 반환 함수
    for i in range(0, k):
        minindex = i
        for j in range(i+1, len(n)):
            if n[minindex] < n[j]:
                minindex = j
        n[i], n[minindex] = n[minindex], n[i]
    return n[k-1]


T = int(input())
for case in range(1, T+1):
    N = int(input())
    x = list(map(int, input().split()))
    n = []
    for i in range(1, 6):
        n.append(select_high(x, i))
        n.append(select_low(x, i))  # 번갈아 입력
    print(f"#{case}", *n)

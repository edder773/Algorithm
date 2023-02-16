def search(arr):  # Parametric Search
    start = 1
    end = max(x)
    while start <= end:
        middle = (start + end) // 2
        num = 0
        for i in x:
            num += i//middle
        if num >= N:
            start = middle + 1
        else:
            end = middle - 1
    return (end)


K, N = map(int, input().split())
x = [0]*K
for w in range(K):
    x[w] = int(input())
print(search(x))

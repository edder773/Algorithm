def binarysearch(a, n, key):
    start = 0
    end = n-1
    cnt = 0
    while start <= end:
        cnt += 1
        middle = (start + end)//2
        if a[middle] == key:
            return cnt
        elif a[middle] > key:
            end = middle
        else:
            start = middle
    return 0


T = int(input())
for case in range(1, T+1):
    P, A, B = map(int, input().split())
    arr = [i for i in range(1, P+1)]
    if binarysearch(arr, P, A) < binarysearch(arr, P, B):
        result = 'A'
    elif binarysearch(arr, P, A) > binarysearch(arr, P, B):
        result = 'B'
    elif binarysearch(arr, P, A) == binarysearch(arr, P, B):
        result = 0
    print(f'#{case} {result}')

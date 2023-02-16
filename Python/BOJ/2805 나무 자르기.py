def search(arr):  # Parametric Search
    start = 1  # 1부터
    end = max(x)  # 최대치까지
    while start <= end:
        middle = (start + end) // 2  # 중간값을 기준으로
        num = 0  # 나무 갯수 0부터
        for i in x:
            if i-middle > 0:  # 높이에서 중간을 뺀게 양수면
                num += (i-middle)  # 나무 갯수 저장
        if num >= M:  # 목표치보다 크면
            start = middle + 1  # +1
        else:
            end = middle - 1
    return end  # 최종 높이값 반환


N, M = map(int, input().split())
x = list(map(int, input().split()))
print(search(x))

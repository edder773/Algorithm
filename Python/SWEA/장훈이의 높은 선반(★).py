def backtracking(a, sum_h):
    global result
    if sum_h >= result:  # 지금 하는 합이 결과보다 크면
        return  # 끝
    if sum_h >= B:  # 선반보다 높아
        result = min(result, sum_h)  # sum_h가 더작으면 result에 추가해
        return
    for i in range(a, N):  # 부분 집합을 찾아보자
        backtracking(i+1, sum_h + height[i])

T = int(input())
for case in range(1, T + 1):
    N, B = map(int, input().split())
    height = list(map(int, input().split()))
    result = float('inf')
    backtracking(0,0)
    print(f'#{case} {result - B}')
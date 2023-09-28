import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
result = [0]
dp = [0]*(N+1)
for i in range(N):  # 각 값에 대해
    if result[-1] < A[i]:  # 끝값보다 크면
        result.append(A[i])  # 집어 넣고
        dp[i+1] = len(result)-1
    else:  # 작으면
        left, right = 0, len(result)  # 이분 탐색을 해보자
        while left <= right:
            mid = (left + right) // 2
            if result[mid] < A[i]:
                left = mid + 1
            else:
                right = mid - 1
        result[left] = A[i]
        dp[i+1] = left

print(len(result) - 1)
way = []
temp = max(dp)
A = [0] + A
for i in range(N, 0, -1):
    if dp[i] == temp:
        way.append(A[i])
        temp -= 1
print(*way[::-1])
# 다이나믹 프로그래밍 (1 -> X)
# 상대적으로 느린 속도
import sys
X = int(sys.stdin.readline())
dp = [0]*(X+1)
for i in range(2,X+1):
    dp[i] = dp[i-1] + 1
    if i % 3 == 0:
        dp[i] = min(dp[i//3]+1, dp[i])
    if i % 2 == 0:
        dp[i] = min(dp[i//2]+1, dp[i])

print(dp[X])

# X -> 1 탐색
# 상대적으로 빠른 속도
import sys
X = int(sys.stdin.readline())
arr = [0] * (X+1)
dp = [X]
if X == 1:
    print(0)
else :
    while not arr[1]:
        temp = []
        for i in dp:
            if i % 3 == 0 and not arr[i//3]:
                arr[i//3] = arr[i] + 1
                temp.append(i//3)
            if i % 2 == 0 and not arr[i//2]:
                arr[i//2] = arr[i] + 1
                temp.append(i//2)
            if arr[i-1] == 0:
                arr[i-1] = arr[i] + 1
                temp.append(i-1)
        dp = temp
    print(arr[1])

# 향상된 다이나믹 프로그래밍
# 중복을 제외하기에 빠른속도 및 적은 메모리 소비
def find(n):
    if n in dp.keys():
        return dp[n]

    if n % 3 == 0 and n % 2 == 0:
        dp[n] = min(find(n//3) +1, find(n//2) + 1)
    elif n % 3 == 0:
        dp[n] = min(find(n//3) +1, find(n-1) + 1)
    elif n % 2 == 0:
        dp[n] = min(find(n//2) +1, find(n-1) + 1)
    else : 
        dp[n] = find(n-1) + 1
    return dp[n]

import sys
X = int(sys.stdin.readline())
dp = {1:0}
print(find(X))

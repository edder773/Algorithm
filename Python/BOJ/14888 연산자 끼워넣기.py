def find(n, result):
    global plus, minus, multi, divide, maxValue, minValue
    if n == N:
        maxValue = max(maxValue, result)
        minValue = min(minValue, result)
        return
    if plus: # 더하기에 대한 백트래킹
        plus -= 1
        find(n+1, result + nums[n])
        plus += 1
    if minus: # 빼기에 대한 백트래킹
        minus -= 1
        find(n+1, result - nums[n])
        minus += 1
    if multi: # 곱하기에 대한 백트래킹
        multi -= 1
        find(n+1, result * nums[n])
        multi += 1
    if divide: # 나누기에 대한 백트래킹
        divide -= 1
        find(n+1, int(result / nums[n]))
        divide += 1

import sys
N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
plus, minus, multi, divide = map(int,sys.stdin.readline().split()) #더하기, 빼기, 곱하기, 나누기
maxValue, minValue = float('-inf'), float('inf') # 최대값 최소값
find(1,nums[0])
print(maxValue)
print(minValue)
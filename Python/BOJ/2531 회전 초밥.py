import sys
N, d, k, c = map(int, sys.stdin.readline().split())
sushi = [int(sys.stdin.readline()) for _ in range(N)]
right, left = 0, 0
result = 0

while left < N:
    right = left + k
    temp = set()
    flag = 0
    for i in range(left, right):
        i %= N
        temp.add(sushi[i])
        if sushi[i] == c:
            flag = 1
    cnt = len(temp)
    if flag == 0:
        cnt += 1    
    result = max(result, cnt)
    left += 1
print(result)
def find(a, b, n, num):
    if n == 6:
        result.add(num)
        return
    
    for dy, dx in move:
        ny, nx = a + dy, b + dx
        if 0 <= ny < 5 and 0 <= nx < 5:
            find(ny, nx, n+1, num + nums[ny][nx])

import sys
result = set()
nums = [list(sys.stdin.readline().split()) for _ in range(5)]
move = [[0,1],[0,-1],[1,0],[-1,0]]

for i in range(5):
    for j in range(5):
        find(i, j, 0, '')

print(len(result))
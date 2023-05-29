import sys
N = int(sys.stdin.readline())
happy, unhappy = [], []
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    if b-a >= 0:
        happy.append((a,b))
    else :
        unhappy.append([a,b])
happy.sort(key = lambda x: (x[0], -x[1])) # x[1] > x[0]인 내용물을 x[0]을 기준으로 오름차순, x[1]을 기준으로 내림차순 정렬 
unhappy.sort(key = lambda x: (-x[1], x[0])) # x[1] < x[0]인 내용물을 x[1]을 기준으로 내림차순, x[0]을 기준으로 오름차순 정렬
fun = 0
result = 1 
for y, x in happy + unhappy:
    if fun < y:
        result = 0
        break
    fun -= y
    fun += x
print(result) 
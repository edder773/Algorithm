import sys
N, L = map(int, sys.stdin.readline().split())
# 웅덩이 끝을 기준으로 정렬
pool = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(N)], key = lambda x : (x[1],x[0]))
plate = pool[0][0] # 널판지 위치
result = 0 # 널판지 개수
for start, end in pool: # 웅덩이 범위를 찾자
    if plate < start: # 널판지가 시작점 보다 작으면 
        plate = start # 널판지 시작
    x = end - plate # 널판지 시작점부터 웅덩이 끝 차이
    if x > 0 : # 널판지가 끝보다 앞에 있어야함
        if x % L == 0:
            result += x//L
            plate += x # 널판지 덮었으니 그만큼 널판지 위치 이동
        else :
            result += x//L + 1
            plate += (x//L + 1)*L
print(result)
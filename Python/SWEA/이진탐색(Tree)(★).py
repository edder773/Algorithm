def binary(a, b):
    global cnt
    if a <= b:
        binary(a*2, b) #재귀로 왼쪽 아래로 내려갈 수 없을때까지 탐색
        tree[a] = cnt  # tree[a]에 cnt 입력
        cnt += 1
        binary(a*2 + 1, b)

# 트리 탐색시 왼쪽아래는 인덱스*2 / 오른쪽은 인덱스*2+1
T = int(input())
for case in range(1, T+1):
    N = int(input())
    tree = [0] * (N + 1) # 1~N까지 넣을 트리 생성
    cnt = 1
    binary(1, N)
    print(f'#{case} {tree[1]} {tree[N//2]}')
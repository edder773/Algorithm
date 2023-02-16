def my_max(n):
    a = n[0]
    for w in range(len(n)):
        if a < n[w]:
            a = n[w]
    return a


for case in range(10):
    T = int(input())
    x = [list(input()) for _ in range(100)]
    x_low = list(zip(*x))  # 열로 이루어진 행렬 생성

    temp = []
    for i in range(100):
        for j in range(100):
            for k in range(100):
                if j != k+1:
                    if x[i][j:k+1] == x[i][j:k+1][::-1]:  # 가로 열에 대한 회문 찾기
                        temp += [len(x[i][j:k+1])]
                    if x_low[i][j:k+1] == x_low[i][j:k+1][::-1]:  # 세로 열에 대한 회문 찾기
                        temp += [len(x[i][j:k+1])]
    print(f'#{T} {my_max(temp)}')

T = int(input())
for case in range(1, T+1):
    N, M = map(int, input().split())
    x = [list(input()) for _ in range(N)]  # 가로 문자열 리스트
    y = list(zip(*x))  # 세로 문자열 리스트
    num = 0
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if x[i][j:k+1] == x[i][j:k+1][::-1]:  # 자른범위가 회문일 경우
                    if num < len(x[i][j:k+1]):  # 그 길이가 기존 num보다 클 경우
                        num = len(x[i][j:k+1])  # num에 숫자 입력
                        data = x[i][j:k+1]  # data에 회문 반환
                        break
                if y[i][j:k + 1] == y[i][j:k + 1][::-1]:
                    if num < len(y[i][j:k + 1]):
                        num = len(y[i][j:k + 1])
                        data = y[i][j:k + 1]
                        break
    print(f'#{case}', ' ', *data, sep='')

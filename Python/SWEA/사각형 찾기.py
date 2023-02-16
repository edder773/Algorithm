T = int(input())
for case in range(1, T+1):
    N = int(input())
    x = [list(map(int, input().split())) for _ in range(N)]
    temp = []

    for i in range(N):
        cnt = 0
        for j in range(N):
            if x[i][j] == 1:  # 행렬 요소가 1일 경우
                cnt += 1  # cnt에 1 증가
            if x[i][j] == 0 and cnt > 0:  # 행렬 요소 1을 지나(cnt>0) 행렬 요소 0을 만날 경우
                temp += [cnt]  # temp에 1값 갯수 저장
                cnt = 0
    num = 0
    for k in temp:
        a = k*(temp.count(k))  # temp에 같은 요소 갯수 * 요소 값 => 사각형 넓이
        if num < a:
            num = a  # 사각형 넓이 중 최대값
    print(f'#{case} {num}')

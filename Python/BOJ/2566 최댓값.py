temp_matrix = []
for _ in range(9):
    N = list(map(int, input().split()))
    temp_matrix.append(N)  # 배열 리스트
x = 0
y = 0
N_max = 0
for i in range(9):
    for j in range(9):
        if temp_matrix[i][j] >= N_max:  # 최대값 구하기
            N_max = temp_matrix[i][j]
            x = i+1  # 최대의 행
            y = j+1  # 최대의 열
print(N_max)
print(x, y)

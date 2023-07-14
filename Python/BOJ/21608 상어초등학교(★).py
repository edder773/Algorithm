# 조건 0 : |r1-r2|+|c1-c2|=1을 만족하는 두 칸 = 인접한 칸 (즉 +칸)
# 조건 1 : 빈 칸중 좋아하는 학생이 인접한 칸에 제일 많은 칸으로 자리를 정함
# 조건 2 : 조건1이 여러개면 인접 칸 중에 빈 칸이 가장 많은 칸으로 자리를 정함
# 조건 3 : 조건2도 여러개면 행번호가 가장 작 칸, 그래도 여러개면 열이 작은 칸
# 조건 4 : 만족도를 구해보자 -> if 좋아하는학생수 == 0 0 else 10**배치 완료 후 인접 칸에 좋아하는 학생의 수-1

def check(): # 좋아하는 학생 수와 빈칸이 몇명 인지 체크, 각각의 최대값 구하기
    result = []
    for y in range(N):
        for x in range(N):
            if classroom[y][x] == 0:
                likes, empty = 0, 0
                for dy, dx in move:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < N and 0 <= nx < N :
                        if classroom[ny][nx] in like: # 좋아하는 학생 수
                            likes += 1
                        if classroom[ny][nx] == 0: # 빈자리 수
                            empty += 1
                result.append([y,x,likes, empty])
    return sorted(result, key=lambda x:(-x[2],-x[3],x[0],x[1])) # like, empty 내림차순, 위치 열, 행순 오름차순 정렬

import sys
N = int(sys.stdin.readline())
classroom = [[0]*N for _ in range(N)]
move = [[0,1],[1,0],[-1,0],[0,-1]]
student_like = {} # 좋아하는 학생 매치시켜주기
for _ in range(N*N):
    num, *like = map(int, sys.stdin.readline().split())
    student_like[num] = like
    x = check()
    classroom[x[0][0]][x[0][1]] = num

result = 0
for y in range(N):
    for x in range(N):
        temp = 0
        for dy, dx in move:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0<= nx < N:
                if classroom[ny][nx] in student_like[classroom[y][x]]: # 좋아하는 학생 번호가 있으면
                    temp += 1 # 학생 수 체크
        if temp > 0 : # 좋아하는 학생이 있다면
            result += 10**(temp-1) # 학생 수에 해당하는 값만큼 증가
print(result)
            

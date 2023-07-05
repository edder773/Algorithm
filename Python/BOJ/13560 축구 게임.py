# 승부차기 진행 -> 유효 점수가 나올 수 있는지 없는지 체크
# 전체 경우의 수는 nC2 = n(n-1)/2
# 즉, 정렬후 하나씩 더해나 간 팀 점수가 경우의 수보다 작아야 성립

import sys
n = int(sys.stdin.readline())
teams = sorted(list(map(int,sys.stdin.readline().split())))
score, result = 0, 1
if sum(teams) != n*(n-1) // 2:
    result = -1
else :
    for i in range(n):
        score += teams[i]
        if i*(i+1) // 2 > score:
            result = -1

print(result)
import sys
S = sys.stdin.readline().strip()
a = S.count('a') # a의 갯수
S += S[:a-1] # a개의 인덱스만큼 추가로 뒤에 더해주기 (초과 인덱스 고려)

result = int(10e9)
for i in range(len(S) - (a-1)) :
    result = min(result, S[i:i+a].count('b'))  # b의 갯수가 최소인 구간 찾기
print(result)
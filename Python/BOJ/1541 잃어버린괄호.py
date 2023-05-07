import sys
S = sys.stdin.readline().strip().split('-') # - 기준으로 괄호를 치면 최소로 만들 수 있음
temp = []
for i in S: # 각 요소에 대해
    cnt = 0
    for j in i.split('+'): # +로 짼 요소들을
        cnt += int(j) # 더하고
    temp.append(cnt) # 모아주자
# 모아준 temp들을 맨 앞 인덱스 제외하고 전부 빼면 최소값
result = temp[0]
for i in temp[1:]:
    result -= i
print(result)
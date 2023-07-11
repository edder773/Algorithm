import sys
S = list(sys.stdin.readline().strip())
P = list(sys.stdin.readline().strip())
result, start, end = 0, 0, 0
while True:
    if start==len(P): 
        break
    for i in range(len(S)-(end-start)): #길이만큼의 문자열 있는지
        if S[i:i+(end-start)+1] == P[start:end+1]: #있다면 길이 1을 늘려서 한번더 탐색
            end+=1
            break
    else: #없다면 결과값, 문자 인덱싱 갱신
        result+=1
        end-=1
        start = end+1
        end = start
print(result)

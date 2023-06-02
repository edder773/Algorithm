import sys
N = int(sys.stdin.readline())
stack = []
result = 0
for i in range(N):
    x = int(sys.stdin.readline())
    while stack and stack[-1][0] < x: # 다음사람이 기존 스택보다 크면
        result += stack.pop()[1] # 그동안 누적된 횟수 만큼 + 1 
    
    if not stack: # 스택이 비었으면
        stack.append([x,1]) # 추가
    
    else : # 스택이 있고
        if stack[-1][0] == x: #만약 크기가 x랑 같다면
            temp = stack.pop()[1] # 빼서
            result += temp # 누적횟수 만큼 더하고
            if stack :
                result += 1
            stack.append([x, temp + 1]) # 다시 넣기
        else :
            stack.append([x, 1])
            result += 1
            
print(result)
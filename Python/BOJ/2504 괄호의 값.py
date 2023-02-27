s = list(input())
stack = []
temp = 1 
result = 0

for i in range(len(s)) :
    if s[i] == '(': # 스텍에 (가 들어오면
        stack.append(s[i]) # 스텍에 넣어주고
        temp *= 2 # temp에 2를 곱해줌
    elif s[i] == '[': # 스텍에 [ 가 들어오면
        stack.append(s[i]) # 스텍에 넣어주고
        temp *= 3 # temp에 3을 곱해줌

    elif s[i] == ')': #만약 )를 만났는데
        if not stack or stack[-1] == '[': #스텍이 비었거나 마지막이 [면 
            result = 0 # 0 저장하고 끝냄 (예시 조건)
            break
        if s[i-1] == '(': # 만약 앞에꺼가 (면
            result += temp # 결과 값을 temp에 더해줌
        stack.pop() 
        temp //= 2 # 꺼냈으니 2로 나누자
    
    elif s[i] == ']':
        if not stack or stack[-1] == '(': #스텍이 비었거나 마지막이 (면
            result = 0 # 0 저장하고 끝냄 (예시 조건)
            break
        if s[i-1] == '[': # [는 3짜리니까
            result += temp
        stack.pop()
        temp //= 3 #꺼냈으니 3으로 나누자
if stack:
    print(0)
else :
    print(result)
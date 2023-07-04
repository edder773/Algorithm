import sys
N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
# 카운팅 배열 만들기
A = [0]*1003 
for i in num:  
    A[i] += 1

result = []
i = 0
while sum(A) > 0: # 카운팅 배열이 빌 때 까지
    flag = 1
    if A[i] and A[i+1]: # 현재 값과 다음 값이 존재하면
        for x in range(i+2,1001): # 다음 값은 건너 뛰어야하니 i+2부터
            if A[x]: # 값이 존재하면
                result += [i] * A[i] # 현재 i값에 해당하는 것 전부 결과에 넣고
                A[i] = 0 # 다 넣었으니 0으로 초기화
                result.append(x) # x값 넣어주기
                A[x] -= 1 # x값 넣었으니 하나 빼주기
                flag = 0
                break # 끝내!

        if flag : # 위 for문 다 통과해도 없으면
            result += [i+1]*A[i+1] # 이제 i+1칸에 해당하는 값을 전부 밀어넣고
            A[i+1] = 0 # 0으로 초기화하고
            result += [i]*A[i] # i칸에 해당하는 값을 전부 밀어 넣고
            A[i] = 0 # 0으로 초기화

    else : # 바로 직 후 값 존재 안하면
        result += [i] * A[i] # 해당 i 값 전부 넣어버리기
        A[i] = 0
    i += 1
print(*result)
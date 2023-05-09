import sys
N = int(sys.stdin.readline())
B = list(map(int,sys.stdin.readline().split()))
result = 0
while True: 
    for i in range(N): # 각 값에 대해
        if B[i] % 2: # 홀수면
            B[i] -= 1 # 1을 빼고
            result += 1 # 횟수 + 1
    if sum(B) == 0: # 빼봤더니 전부 0 이면
        break # 끝
    for i in range(N): # 짝수인 애들을
        B[i] /= 2 # 전부 나누고
    result += 1 # 횟수 + 1
print(result)
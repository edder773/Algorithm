import sys
N = sys.stdin.readline().strip()
result = 0
if len(N) == 1: # 1의 자리일때는
    result = int(N) #그냥 바로 출력해!
else : # N이 1의 자리가 아니면
    result = 11 # 11부터 시작해보자 (N=10이면 11자리니까!)
    for i in range(2,10): # N이 최대 1억이니 9까지만 탐색해보자
        if len(N) == i: # N의 자리수를 찾았을 때!
            result += i*(int(N)-(10**(i-1))) #그 숫자의 자리수 *(그 숫자의 자리수-1에 해당하는 숫자 영역)을 해서 더해주자
            break
        else : # 자리수가 다르면
            result += i*(9*10**(i-1))+1 # 자리수에 해당하는 최대 갯수만큼 누적해서 더해놓자!
print(result)
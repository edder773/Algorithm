import sys
T = int(sys.stdin.readline())
for _ in range(T):
    p = list(sys.stdin.readline().strip())
    n = int(sys.stdin.readline())
    arr = sys.stdin.readline()[1:-2].split(',') # 좌우에 [ ]를 잘라주고, ,도 없애주자
    # sys.stdin.readline()으로 값을 받을 경우 끝에 '\'가 추가로 들어오므로 [1:-2]
    cnt = 0 # 뒤집을 횟수 세기 

    if n == 0: 
        arr = [] # n이 0이면 빈 배열!

    for i in p :
        if i == 'R':
            cnt += 1 # 뒤집을 횟수 추가
        elif i == 'D': # D일 경우
            if len(arr) == 0: # arr가 비었다면
                print('error') # 에러출력
                break
            else:
                if cnt % 2 == 0: # 뒤집은 횟수가 짝수면 앞에꺼, 홀수면 뒤에꺼 빼주기
                    arr.pop(0)
                else:
                    arr.pop()
    else:
        if cnt % 2 == 0: # 짝수면 그대로 출력
            print("[" + ",".join(arr)+"]")
        else:
            arr.reverse() # 홀수면 뒤집어서 출력
            print("[" + ",".join(arr)+"]")
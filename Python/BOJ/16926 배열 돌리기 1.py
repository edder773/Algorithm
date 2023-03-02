import sys
N, M ,R = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
for _ in range(R):
    for i in range(min(N,M)//2): # 내부 스핀 도는 갯수
        r, c = N-2*i, M-2*i # 내부로 들어갈수록 상하좌우 2칸씩 줄어듦
        temp = arr[i][i] #시작

        for L in range(i, i+r): # 좌측 / i부터 i+r까지 -> 돌아가는 직사각형의 한변
            spin = arr[L][i] # spin에 arr[L][i] 값을 저장해서
            arr[L][i] = temp # arr[L][i]에 temp값을 넣어주고
            temp = spin # temp 값에 위에서 저장한 spin 값을 넣어줌

        for D in range(i+1, i+c): # 아래쪽 / 위와 동일
            spin = arr[i+r-1][D]
            arr[i+r-1][D] = temp
            temp = spin
        
        for R in range(i+r-2,i-1,-1): # 오른쪽
            spin = arr[R][i+c-1]
            arr[R][i+c-1] = temp
            temp = spin
        
        for U in range(i+c-2, i-1, -1): #위쪽
            spin = arr[i][U]
            arr[i][U] = temp
            temp = spin

for k in arr:
    print(' '.join(map(str,k)))
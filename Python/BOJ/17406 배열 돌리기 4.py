def rotate():
    result = float('inf')
    for case in permutations(oper,K): # 연산의 순서가 랜덤
        arr = deepcopy(arrs)
        for r,c,s in case:
            r, c = r-1, c-1 # 주어진 조건은 1행, 1열부터 이므로
            for i in range(s,0,-1):
                temp = arr[r-i][c+i] # 임시값
                arr[r-i][c-i+1:c+i+1] = arr[r-i][c-i:c+i] # 오른쪽으로 이동

                for U in range(r-i, r+i): #위쪽으로 이동
                    arr[U][c-i] = arr[U+1][c-i]
                
                arr[r+i][c-i:c+i] = arr[r+i][c-i+1:c+i+1] # 왼쪽으로 이동

                for D in range(r+i, r-i, -1): # 아래쪽으로 이동
                    arr[D][c+i] = arr[D-1][c+i]
                
                arr[r-i+1][c+i] = temp #다시 되돌려주기
        for x in arr :
            result = min(result,sum(x))
    return result
                                

import sys
from itertools import permutations
from copy import deepcopy
N,M,K = map(int,sys.stdin.readline().split())
arrs = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
oper = [list(map(int,sys.stdin.readline().split())) for _ in range(K)]
print(rotate())
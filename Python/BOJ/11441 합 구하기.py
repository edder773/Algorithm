import sys
N = int(sys.stdin.readline())
A = [0]+list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
for i in range(1,N+1):
    A[i] += A[i-1] # 리스트 A를 누적합으로 변환
for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    print(A[j]-A[i-1]) # 원하는 부분까지의 합 출력
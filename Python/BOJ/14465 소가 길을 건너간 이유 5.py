import sys
N, K, B = map(int, sys.stdin.readline().split())
broken = [0]*(N+1)
for _ in range(B):
    m = int(sys.stdin.readline())
    broken[m] = 1

for i in range(N):
    broken[i+1] += broken[i]

result = B # 고쳐야하는 최대 갯수
for i in range(K,N+1):
    result = min(result, broken[i] - broken[i-K])
print(result)
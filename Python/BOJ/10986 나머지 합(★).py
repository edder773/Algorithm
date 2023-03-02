import sys
N, M = map(int, sys.stdin.readline().split())
x = list(map(int, sys.stdin.readline().split()))+[0]
r = [0]*M
for i in range(N):
    x[i] += x[i-1] # 누적합 
    r[x[i] % M] += 1 # 누적합을 M으로 나눈 나머지를 인덱스로 해당 인덱스에 해당하는 r값 1씩 증가
cnt = r[0]

for i in r:
    cnt += i*(i-1)//2 # r의 값에서 2개를 조합하여 뽑을 때 값

print(cnt)
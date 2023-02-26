import sys
N = int(input())
x = [sorted(list(map(int, sys.stdin.readline().split())))[-1]] # 제일 큰애 저장
for i in range(N-1):
    table = sorted(list(map(int, sys.stdin.readline().split())) + x)
    x = table[-N:]
    print(table)
    print(x)
print(x[0])
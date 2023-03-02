import sys
N = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().split()))
temp = [0]*100
stack = []
result = [-1 for _ in range(N)]

for k in x:
    temp[k] += 1

for i in range(N):
    while stack and temp[x[stack[-1]]] < temp[x[i]]:
        result[stack.pop()] = x[i]
    stack.append(i)
print(temp)
print(result)

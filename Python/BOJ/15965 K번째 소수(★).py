import sys
N = int(sys.stdin.readline())
M = 7400000
array = [0]*(M+1)
for i in range(2, int(M**0.5)+1):
    if array[i] == 0:
        for j in range(i*i,M+1,i):
            array[j] = 1
x = [i for i in range(2,M+1) if array[i] == 0]
print(x[N-1])
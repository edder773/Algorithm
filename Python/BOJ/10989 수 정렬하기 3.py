import sys
n = int(input())
num = [0]*10000
for i in range(n):
    num[int(sys.stdin.readline())-1] += 1

for i in range(len(num)):
    if n != 0:
        for j in range(num[i]):
            print(i+1)

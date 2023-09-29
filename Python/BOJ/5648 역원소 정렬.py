import sys
n, *num = sys.stdin.readline().strip().split()
while len(num) < int(n):
    num.extend(list(sys.stdin.readline().strip().split()))
num = sorted([int(i[::-1]) for i in num])
print(*num,sep='\n')
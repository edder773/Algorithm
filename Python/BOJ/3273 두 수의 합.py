import sys
n = int(sys.stdin.readline())
a = sorted(list(map(int, sys.stdin.readline().split())))
x = int(sys.stdin.readline())
start, end = 0, n-1 
cnt = 0
while start < end:
    if a[start] + a[end] == x:
        cnt += 1
        start += 1
    elif a[start] + a[end] < x:
        start += 1
    else :
        end -=1
print(cnt)
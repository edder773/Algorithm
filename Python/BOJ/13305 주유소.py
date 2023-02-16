import sys
N = int(sys.stdin.readline())
line = list(map(int, sys.stdin.readline().split()))
price = list(map(int, sys.stdin.readline().split()))


a = line[0]*price[0]
b = price[0]

for i in range(1, N-1):
    if b > price[i]:
        b = price[i]
    a += b*line[i]
print(a)

import sys
num = 1000001
fn = [1] * (num)
gn= [0]*(num)

for i in range(2, num):
    j = 1
    while i*j < num:
        fn[i*j] += i
        j += 1

for i in range(1, num):
    gn[i] = gn[i-1] + fn[i]

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    print(gn[n])
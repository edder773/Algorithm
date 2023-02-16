import sys


def prime_list(n):
    array = [True] * n
    m = int(n**0.5)
    for i in range(2, m+1):
        if array[i] == True:
            for j in range(i+i, n, i):
                array[j] = False
    return array


ran = prime_list(250000)
cnt = 0

while True:
    x = int(sys.stdin.readline())
    if x == 0:
        break
    elif x == 1:
        cnt = 1
    for i in range(x+1, 2*x):
        if ran[i] == True:
            cnt += 1
    print(cnt)
    cnt = 0

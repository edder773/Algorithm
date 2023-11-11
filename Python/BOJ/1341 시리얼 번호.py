def same(n):
    result = 0
    for i in n:
        if i.isdigit():
            result += int(i)
    return result


import sys
N = int(sys.stdin.readline())
serial = list(sys.stdin.readline().strip() for _ in range(N))
serial.sort(key = lambda x : (len(x), same(x), x))
for i in serial:
    print(i)
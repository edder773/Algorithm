import sys
N = int(sys.stdin.readline())
result = []

for i in range(1, N+1):
    now, next = N, i
    temp = [N, i]
    while now >= next:
        x = now - next
        temp.append(x)
        now, next = next, x
        if len(temp) > len(result):
            result = temp

print(len(result))
print(*result)
import sys
n, m = map(int, sys.stdin.readline().split())
T = int(sys.stdin.readline())
w, h = [0, n], [0, m]
for _ in range(T):
    x, line = map(int,sys.stdin.readline().split())
    if x == 0:
        h.append(line)
    else:
        w.append(line)

w.sort()
h.sort()

result = 0
for i in range(len(w) -1):
    for j in range(len(h) - 1):
        x = w[i+1] - w[i]
        y = h[j+1] - h[j]
        result = max(result, x*y)
print(result)

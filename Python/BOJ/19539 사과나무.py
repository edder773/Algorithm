import sys
N = int(sys.stdin.readline())
h = list(map(int, sys.stdin.readline().split()))
cnt = sum(h) // 3
if (sum(h) % 3):
    print("NO")
else:
    for i in h:
        cnt -= (i//2)
        print(cnt)
    if cnt > 0:
        print("NO")
    else:
        print("YES")
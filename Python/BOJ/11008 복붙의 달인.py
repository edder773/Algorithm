import sys
T = int(sys.stdin.readline())
for _ in range(T):
    s, p = sys.stdin.readline().strip().split()
    s = s.replace(p,'*')
    print(len(s))
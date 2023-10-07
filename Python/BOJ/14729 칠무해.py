import sys
N = int(sys.stdin.readline())
scores = sorted([float(sys.stdin.readline()) for _ in range(N)])
for i in range(7):
    print("{:.3f}".format(scores[i]))
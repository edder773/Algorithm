import sys
N = int(sys.stdin.readline())
P = [0]*N
for i in range(N):
    words = sys.stdin.readline().strip()
    P[i] = (len(words), words)
O = list(set(P))
O.sort(key=lambda x: x[0])
O.sort()
for j in range(len(O)):
    print(O[j][1])

import sys
S = sys.stdin.readline().strip()
result = []
for i in range(len(S)):
    result.append(S[i:])
result.sort()
for i in result:
    print(i)
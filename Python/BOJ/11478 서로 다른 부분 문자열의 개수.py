import sys
S = list(sys.stdin.readline().strip())
temp = []

for i in range(len(S)):
    for j in range(len(S)):
        temp.append(''.join(S[i:i+j+1]))
print(len(set(temp)))

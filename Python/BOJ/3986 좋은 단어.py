import sys
N = int(sys.stdin.readline())
result = 0
for _ in range(N):
    S = sys.stdin.readline().strip()
    stack = []
    for i in range(len(S)):
        if not stack:
            stack.append(S[i])
        elif stack[-1] == S[i] :
            stack.pop()
        else:
            stack.append(S[i])
    if not stack:
        result += 1
print(result)
def manachers(S, N):
    A = [0] * N
    r, p = 0, 0
    for i in range(N):
        if i <= r:
            A[i] = min(A[2 * p - i], r - i)
        while i - A[i] - 1 >= 0 and i + A[i] + 1 < N and S[i - A[i] - 1] == S[i + A[i] + 1]:
            A[i] += 1
        if r < i + A[i]:
            r = i + A[i]
            p = i
    return A

import sys
S = sys.stdin.readline()
N = len(S)
s = ""
for i in range(N):
    s += '#'
    s += S[i]
s += '#'
A = manachers(s, len(s))
print(max(A))
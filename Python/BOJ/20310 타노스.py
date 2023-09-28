import sys
S = list(sys.stdin.readline().strip())
N, zero, one = len(S), S.count('0')//2, S.count('1')//2
for i in range(N-1,-1,-1):
    if zero and S[i] == '0':
        S[i] = 'x'
        zero -= 1
for i in range(N):
    if one and S[i] == '1':
        S[i] = 'x'
        one -= 1

result = ''
for i in S:
    if i != 'x':
        result += i
print(result)
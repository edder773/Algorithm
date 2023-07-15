import sys
S = sys.stdin.readline().strip()
a, n = S[0], len(S)
for i in range(1, n):
    if a[-1] < S[i]: # a의 마지막 문자가 S[i] 보다 작으면
        a = S[i] + a # S[i] 뒤에 + a
    else: 
        a += S[i] # 아니면 a 뒤에 + S[i]
print(a[::-1])
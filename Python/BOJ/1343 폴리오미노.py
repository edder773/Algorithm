import sys
S = sys.stdin.readline().strip()
S = S.replace('XXXX', 'AAAA')
S = S.replace('XX', 'BB')

if 'X' in S :
    print(-1)
else:
    print(S)
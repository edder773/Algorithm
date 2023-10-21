def find(n):
    if len(lotto) == 6:
        print(*lotto)
        return
    
    for i in range(n,k):
        if S[i] not in lotto:
            lotto.append(S[i])
            find(i)
            lotto.pop()

import sys
while True:
    k, *S = list(map(int, sys.stdin.readline().split()))
    lotto = []
    if k == 0:
        break
    find(0)
    print()
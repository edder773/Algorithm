import sys
from itertools import combinations
L, C = map(int, sys.stdin.readline().split())
alpha = sorted(list(sys.stdin.readline().strip().split()))
vow = "aeiou"
consonant = "bcdfghjklmnpqrstvwxyz"
for password in combinations(alpha,L):
    cnt = 0
    for i in password :
        if i in consonant:
            cnt += 1
            if cnt == 2:
                break
        if i in vow :
            print("".join(password))
            break
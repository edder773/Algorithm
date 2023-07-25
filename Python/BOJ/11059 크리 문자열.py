import sys
S = sys.stdin.readline().strip()
N = len(S)
result = 0
for i in range(N):
    left , right = i, i+1
    Lsum, Rsum = 0, 0
    while left >= 0 and right < N:
        Lsum += int(S[left])
        Rsum += int(S[right])
        if Lsum == Rsum:
            result = max(result, right-left+1)
        left -= 1
        right += 1
print(result)
# import sys
# N, M = map(int, sys.stdin.readline().split())
# A = list(map(int, sys.stdin.readline().split()))
# B = list(map(int, sys.stdin.readline().split()))
# temp = []

# for i in range(N):
#     if A[i] not in B:
#         temp.append(A[i])

# for j in range(M):
#     if B[j] not in A:
#         temp.append(B[j])

# print(len(temp))

import sys
N, M = map(int, sys.stdin.readline().split())
A = set(map(int, sys.stdin.readline().split()))
B = set(map(int, sys.stdin.readline().split()))

c = A-B
d = B-A
print(len(c)+len(d))

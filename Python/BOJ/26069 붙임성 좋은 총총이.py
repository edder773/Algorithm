import sys
N = int(sys.stdin.readline())
name = ['ChongChong']
for _ in range(N):
    A, B = sys.stdin.readline().strip().split()
    if A in name:
        if B not in name :
            name.append(B)
    elif B in name:
        if A not in name :
            name.append(A)
print(len(name))
def make(start, end, index):
    if start == end:
        tree[index] = T[start-1]
        return tree[index]
    mid = (start+end) // 2
    tree[index] = make(start, mid, index*2) + make(mid + 1, end, index*2+1)
    return tree[index]

def find(start, end, index, left, right):
    if start > right or left > end:
        return 0

    if start >= left and end <= right:
        return tree[index]
    
    mid = (start + end) // 2
    return find(start, mid, index*2, left, right) + find(mid+1, end, index*2+1, left, right)

def update(start, end, index, newIdx, value):
    if start > newIdx or end < newIdx:
        return
    tree[index] += value

    if start == end:
        return
    
    mid = (start + end)//2
    update(start, mid, index*2, newIdx, value)
    update(mid+1, end, index*2+1, newIdx, value)

import sys
N, M, K = map(int, sys.stdin.readline().split())
tree = [0]*(N*4)
T = [int(sys.stdin.readline()) for _ in range(N)]
make(1, N, 1)

for _ in range(M+K):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        temp = c - T[b-1]
        T[b-1] = c
        update(1, N, 1, b, temp)
    elif a == 2:
        print(find(1,N,1,b,c))

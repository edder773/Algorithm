def preorder(a):
    if a != '.':
        preorders.append(a)
        preorder(tree[a][0])
        preorder(tree[a][1])

def inorder(a):
    if a != '.':
        inorder(tree[a][0])
        inorders.append(a)
        inorder(tree[a][1])

def postorder(a):
    if a != '.':
        postorder(tree[a][0])
        postorder(tree[a][1])
        postorders.append(a)

import sys
N = int(sys.stdin.readline())
tree = {}
preorders = []
inorders  = []
postorders = []

for _ in range(N):
    root, left, right = sys.stdin.readline().split()
    tree[root] = [left, right]

preorder('A'), inorder('A'), postorder('A')

print(*preorders, sep="")
print(*inorders, sep="")
print(*postorders, sep="")
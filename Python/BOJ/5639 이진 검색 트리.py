# 루트노드 : 50
# 왼쪽 자식 : 30, 24, 5, 28, 45
# 오른쪽 자식 : 98, 52, 60

def postorders(left, right):
    if left > right:
        return
    mid = right + 1
    for i in range(left+1, right+1):
        if preorder[i] > preorder[left]:
            mid = i
            break

    postorders(left + 1, mid -1)
    postorders(mid, right)
    postorder.append(preorder[left])

import sys
sys.setrecursionlimit(100000)
preorder = []
postorder = []
while True:
    try : 
        preorder.append(int(sys.stdin.readline()))
    except :
        break

postorders(0, len(preorder)-1)
for i in postorder:
    print(i)
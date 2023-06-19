def find(inL, inR, postL, postR): # 각 중위, 후위 왼쪽, 오른쪽
    if inL > inR or postL > postR:
        return 
        
    preorder.append(postorder[postR])
    a = p[postorder[postR]] # 루트 노드의 중위 순회에서 몇번째 방문인지 체크
    node = a - inL #왼쪽 서브트리 노드 수

    # 전위 순회이므로 왼쪽 -> 오른쪽
    # 왼쪽 서브트리
    find(inL, a - 1, postL, postL + node - 1)
    # 오른쪽 서브트리
    find(a + 1, inR, postL + node, postR - 1)

import sys
sys.setrecursionlimit(1000000)
N = int(sys.stdin.readline())
inorder = list(map(int, sys.stdin.readline().split()))
postorder = list(map(int, sys.stdin.readline().split()))
preorder = []
p = [0]*(N+1)

for i in range(N):
    p[inorder[i]] = i

find(0, N-1, 0, N-1)
print(*preorder)
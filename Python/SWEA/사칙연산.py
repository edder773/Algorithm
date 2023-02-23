for case in range(1, 11):
    N = int(input())
    tree = [0]*(N+1)
    temp = [[0]]
    for _ in range(N):
        a, b, *x = input().split()
        if b == '-' or b == '+' or b == '*' or b== '/':
            tree[int(a)] = b
        else :
            tree[int(a)] = int(b)
        temp.append(x)
    for i in range(N-1, 0, -1):
        if tree[i] == '-':
            tree[i] = (tree[int(temp[i][0])])-(tree[int(temp[i][1])])
        if tree[i] == '/':
            tree[i] = (tree[int(temp[i][0])])/(tree[int(temp[i][1])])
        if tree[i] == '+':
            tree[i] = (tree[int(temp[i][0])])+(tree[int(temp[i][1])])
        if tree[i] == '*':
            tree[i] = (tree[int(temp[i][0])])*(tree[int(temp[i][1])])
    print(f'#{case} {int(tree[1])}')
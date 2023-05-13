import sys
N = int(sys.stdin.readline())
result = {}
for _ in range(N):
    employee, check = sys.stdin.readline().strip().split()
    if (check == 'enter'):
        result[employee] = check
    else :
        del result[employee]
print('\n'.join(sorted(result,reverse=True)))
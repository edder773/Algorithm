import sys
N = int(sys.stdin.readline())
name = [sys.stdin.readline().strip() for _ in range(N)]
asname = sorted(name)
dename = sorted(name,reverse=True)
if name == dename :
    print('DECREASING')
elif name == asname :
    print('INCREASING')
else:
    print('NEITHER')
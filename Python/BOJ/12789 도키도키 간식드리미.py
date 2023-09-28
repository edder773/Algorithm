import sys
N = int(sys.stdin.readline())
student = list(map(int, sys.stdin.readline().split()))
stack = []
num = 1
for i in student:
    if i == num:
        num += 1
    elif stack and stack[-1] == num:
        stack.pop()
        num += 1
    else:
        stack.append(i)

    while stack:
        if stack[-1] == num:
            num += 1
            stack.pop()
        else:
            break
if stack:
    print("Sad")
else:
    print("Nice")

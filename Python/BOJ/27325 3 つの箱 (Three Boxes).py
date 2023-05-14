import sys
N = int(sys.stdin.readline())
S = sys.stdin.readline().strip()
p = 1
result = 0
for i in S:
    if i == 'L':
        if p == 1 :
            p = 1
        else :
            p -= 1
    if i == 'R':
        if p == 3:
            p = 3
            result +=1
        else :
            p += 1
            if p == 3:
                result +=1
print(result)
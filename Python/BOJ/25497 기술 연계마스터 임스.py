import sys
N = int(sys.stdin.readline())
S = sys.stdin.readline().strip()
r, k = [], []
result = 0
for i in S:
    if i in "123456789":
        result += 1
        
    elif i == "L":
        r.append(i)
    
    elif i == "R":
        if r and r[-1] == "L":
            r.pop()  
            result += 1
        else:
            break
        
    elif i == "S":
        k.append(i)
    
    elif i == "K":
        if k and k[-1] == "S":
            k.pop() 
            result += 1    
        else:
            break
print(result)
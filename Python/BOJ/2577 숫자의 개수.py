A = int(input())
B = int(input())
C = int(input())
x = list(str(A*B*C))
temp = [0]*10
for i in x :
    temp[int(i)] += 1
for j in range(10):
    print(temp[j])

N = list(input())
x = [0]*10
for i in range(len(N)):
    x[int(N[i])] += 1

if x.index(max(x)) == 6 or x.index(max(x)) == 9:
    if x[6]+x[9] % 2 == 1:
        print((x[6]+x[9])//2+1)
    else :
        print((x[6]+x[9])//2)
else :
    print(max(x))
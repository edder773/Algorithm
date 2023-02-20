n = int(input())
x = list(input())
alpha = ['0','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
M = 1234567891
r = 31
y = [0]*n
sums = 0
for i in range(n):
    y[i] = alpha.index(x[i])

for j in range(n):
    sums += y[j]*r**(j)
    H = sums % M
print(H)
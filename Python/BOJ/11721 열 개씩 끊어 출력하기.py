N = list(input())
for i in range(len(N) // 10 + 1):
    print(*N[10*i:10*(i+1)],sep='')

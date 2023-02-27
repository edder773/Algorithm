N,K = map(int,input().split())
nums = [True] * (N+1)
cnt = 0
for i in range(2, N+1): # N까지의 수중
    for j in range(i, N+1, i) : # i 간격으로 N+1 
            if nums[j] == True: # True면
                  nums[j] = False # False
                  cnt += 1
                  if cnt == K:
                        print(j)
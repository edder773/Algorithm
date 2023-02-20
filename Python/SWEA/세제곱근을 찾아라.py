T = int(input())
for case in range(1,T+1):
    n = int(input())
    nums = []
    for i in range(1,int(n**(1/3))+2):
        nums += [i**3]
    if n in nums:
        print(f'#{case} {nums.index(n)+1}')
    else :
        print(f'#{case} {-1}')
T = int(input())
for case in range(1,T+1):
    N = int(input())
    carrot = list(map(int, input().split()))
    crit = N//2 # 기준값
    carrot.sort() # 당근 크기 순서대로 정렬하기 (제일 중요함)
    result = float('inf') #최소 구해주기
    for i in range(N):
        for j in range(N):
            if i < j:
                small = carrot[:i] #작은 상자에 i만큼 넣자
                s = len(small)
                middle = carrot[i:j] #중간 상자에 i~j까지 넣자
                m = len(middle)
                large = carrot[j:] #큰 상자에 나머지 넣자
                l = len(large)
                if middle[0] not in small and large[0] not in middle: #가운데 맨 앞에가 작은거에 있거나, 큰거 맨앞에가 작은거에 있으면 안됨
                    if 0 < s <= crit and 0 < m <= crit and 0 < l <= crit: # 각 상자가 범위 밖을 벗어나도 안됨
                        if result > max(s,m,l)-min(s,m,l): # 각 상자에 든 갯수 차
                            result = max(s,m,l)-min(s,m,l)
    if result == float('inf'):
        print(f'#{case} -1')
    else :
        print(f'#{case} {result}')
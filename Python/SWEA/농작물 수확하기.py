T = int(input())
for case in range(1,T+1):
    N= int(input())
    farm_up = [list(map(int,input())) for _ in range(N//2)] # 가운데 기준 위
    farm_mid = list(map(int,input())) # 한 가운데
    farm_down = [list(map(int, input())) for _ in range(N//2)][::-1] #가운데 기준 아래를 뒤집은 것
    plant = 0

    for i in range(N//2):
        for j in range(N//2-i,N//2+i+1): # 마름모 모양으로
            plant += farm_up[i][j] #위랑
            plant += farm_down[i][j] #아래 역순을 더해주고
    plant += sum(farm_mid) # 가운데를 더해주면
    print(f'#{case} {plant}') # 농작물의 수익이나와요

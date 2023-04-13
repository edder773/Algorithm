import sys
K = int(sys.stdin.readline())
x = [2**i for i in range(21)] # 초콜릿 선택용
for i in x:
    if K <= i: # K 보다 큰 초콜릿을 고르자
        choco = i 
        break
cnt = 0 # 몇번 쪼개야할까?
temp = choco # 쪼개줄 임시의 초콜릿
if K != choco: # 통초콜릿과 사이즈가 다르면
    while K : # 0이 될때 까지 쪼개보자
        temp //= 2 # 쪼갰는데
        if K >= temp: # 원하는 사이즈보다 작으면
            K = K - temp # 그만큼 갉아먹고
            cnt += 1 # 쪼갠 수 증가
        else: # 아니면
            cnt += 1 # 쪼개기만하기
print(choco, cnt)
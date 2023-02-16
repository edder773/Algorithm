T = int(input())

def game(a,b):
    if card[a] == card[b]: #카드가 같으면
        return [min(a , b)] #번호 더 작은 쪽이 win
    elif abs(card[a] - card[b]) == 1: # a랑 b랑 차이가 1이면
        return [a] if card[a] > card[b] else [b] # a의 카드 숫자가 더크면 win a 아니면 b win
    elif abs(card[a] - card[b]) == 2: # a랑 b랑 차이가 2이면
        return [a] if card[a] < card[b] else [b] # a의 카드 숫자가 더작으면 win 아니면 b win

def group(n):
    if len(n) == 1: # 1개가 되면
        return n #n 반환
    middle = (len(n)-1) // 2 + 1 #조건대로 쪼개기
    group1 = n[:middle] #좌측 그룹
    group2 = n[middle:] #우측 그룹

    group1 = group(group1) #다시 좌측 그룹을 2개로 쪼개기
    group2 = group(group2) #다시 우측 그룹을 2개로 쪼개기
    return game(group1[0], group2[0]) #쪼개진 그룹을 게임 시켜 반환

for case in range(1,T+1):
    N = int(input())
    card = list(map(int, input().split()))
    x = [i for i in range(N)] #각 학생 번호
    print(f'#{case} {group(x)[0]+1}')
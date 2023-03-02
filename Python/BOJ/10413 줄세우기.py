def Bubblesort(List): #정렬할 list, 원소 수 N
    global cnt
    for i in range(len(List)-1, 0, -1) : # 범위의 끝
        for j in range(i) :
            if List[j] > List[j+1] : #현재 항이 다음 항보다 클 경우
                List[j], List[j+1] = List[j+1], List[j] #서로의 위치를 바꿔라
                cnt += 1

T = int(input())
for _ in range(T):
    N, *x = map(int,input().split())
    cnt = 0
    Bubblesort(x)
    print(N, cnt)
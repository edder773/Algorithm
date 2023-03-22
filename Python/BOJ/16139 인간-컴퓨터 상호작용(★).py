import sys
S = sys.stdin.readline().strip()
q = int(sys.stdin.readline())
alpha = 'abcdefghijklmnopqrstuvwxyz' #알파벳 모음

temp = {} # 누적합을 저장해줄 딕셔너리
for i in alpha: # 각각의 알파벳에 대해
    cnt = 0 
    temp1 = [0]*len(S) # 누적합을 구해보자
    for j in range(len(S)) : # 범위에서
        if i == S[j] : # 알파뱃 등장하면
            cnt += 1 # 횟수 늘리고
        temp1[j] = cnt # 누적해서 temp1에 저장
    temp[i] = temp1 # 알파벳 : 누적합 리스트 형태로 저장

for _ in range(q):
    a, l, r = sys.stdin.readline().split() 
    l, r = int(l), int(r)
    acc_sum = temp[a] # 우리가 찾고자 하는 알파벳의 누적합을 꺼내오자
    if l > 0: # 0이상이면
        print(acc_sum[r] - acc_sum[l-1]) # 유효 범위에서 제일 큰 거 - 제일 작은 거 이전꺼까지
    else: # 0이면
        print(acc_sum[r]) #유효 범위에서 제일 큰 애 
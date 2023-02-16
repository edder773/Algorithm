T = int(input())
for case in range(1, T+1):
    a = ['b', 'd', 'p', 'q']
    rev_a = ['d', 'b', 'q', 'p']  # 각 b,d,p,q를 뒤집은 값
    x = list(input())
    for i in range(len(x)):
        for j in range(4):
            if x[i] == a[j]:  # x의 원소가 a랑 일치하면
                x[i] = rev_a[j]  # 해당 원소 뒤집어 반환
                break
    print(f'#{case}', ' ', *x[::-1], sep='')  # 순서를 뒤집어서 출력

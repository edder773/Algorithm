T = int(input())
for case in range(1, T+1):
    x = list(input().strip())  # 공백제거한 리스트
    if x == x[::-1]:  # 뒤집은거랑 같다면
        print(f'#{case} 1')
    else:
        print(f'#{case} 0')

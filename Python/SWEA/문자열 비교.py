T = int(input())
for case in range(1, T+1):
    str1 = input()
    str2 = input()
    if str1 in str2:  # str1이 str2에 있으면
        print(f'#{case} 1')
    else:
        print(f'#{case} 0')

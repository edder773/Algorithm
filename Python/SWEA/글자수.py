T = int(input())


def my_max(n):  # 최대값 구하기
    m = n[0]
    for i in range(len(n)):
        if m < n[i]:
            m = n[i]
    return m


for case in range(1, T+1):
    str1 = list(input())  # str1의 문자열
    str2 = list(input())  # str2의 문자열
    temp = []
    for i in range(len(str1)):
        cnt = 0  # 횟수
        for j in range(len(str2)):
            if str1[i] == str2[j]:  # str1의 문자가 str2의 문자와 같은 경우
                cnt += 1  # 횟수 증가
        temp += [cnt]
    print(f'#{case} {my_max(temp)}')

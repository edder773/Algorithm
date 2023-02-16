def sorts(n, k):  # 오름차순 반환
    for i in range(k):
        minindex = i
        for j in range(i+1, len(n)):
            if n[minindex] > n[j]:
                minindex = j
        n[i], n[minindex] = n[minindex], n[i]
    return n[k-1]


T = int(input())

name = ["ZRO", "ONE", "TWO", "THR", "FOR",
        "FIV", "SIX", "SVN", "EGT", "NIN"]  # 각 글자
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # 각 글자에 해당하는 숫자
for case in range(1, T+1):
    tc_num, n = map(str, input().split())
    N = list(map(str, input().split()))
    for i in range(int(n)):
        for j in range(10):
            if N[i] == name[j]:  # N의 i번 인덱스가 name안에 있는 j번 인덱스랑 같으면
                N[i] = num[j]  # N을 숫자로 변환
    sorts(N, int(n))  # 정렬

    for x in range(int(n)):
        for y in range(10):
            if N[x] == num[y]:
                N[x] = name[y]
    print(tc_num)
    print(*N)

T = int(input())
for case in range(1,T+1):
    N = int(input())
    carrot = list(map(int, input().split())) + [0]
    stem, stem_sum = 1, 0
    long_stem, cnt, result = 0, 0, 0
    for i in range(N):
        if carrot[i] < carrot[i+1]: # 다음 당근이 더 크면
            stem += 1 # 줄기 증가
            stem_sum += carrot[i] # 당근 갯수 합
        else :
            stem_sum += carrot[i] # 다음 당근이 작으면 여기까지 당근 합
            if stem > 1: # 줄기가 1개 이상일 때
                if long_stem < stem: # 긴 줄기보다 지금 줄기가 길면
                    long_stem = stem # 긴 줄기는 지금 줄기
                    result = stem_sum # 그 때의 줄기 내용물 합
                elif long_stem == stem and result < stem_sum: # 줄기 사이즈 같은데 새로 들어온게 더 갯수 많으면
                    result = stem_sum # 갯수 저장
                cnt += 1
            stem = 1
            stem_sum = 0

    print(f'#{case} {cnt} {result}')
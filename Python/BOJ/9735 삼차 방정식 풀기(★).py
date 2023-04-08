def find():
    for x in range(1,abs(d)+1): 
        if d % x == 0: # 삼차방정식 근의 관계에 의해 d는 무조건 x의 약수이므로
            if a*x**3 + b*x**2 + c*x + d == 0: # 다음 해를 만족하면 (양수 일 때)
                return x # x 반환
            elif -a*x**3 + b*x**2 -c*x + d == 0: # 다음 해를 만족하면 (음수 일 때 x는 -니까)
                return -x # -x 반환
    return 0 # 없으면 0으로 반환

import sys
T = int(sys.stdin.readline())
for _ in range(T):
    a, b, c, d = map(int, sys.stdin.readline().split())
    x, result = find(), set()
    a, b, c = a, a*x + b, a*x**2 + b*x + c # 정수 해 x를 아니, 이걸 토대로 2차 방정식으로 만들어주자
    if b**2 - 4*a*c < 0: # 판별식 (근이 1개)
        result.add(x) # x 하나 뿐
    elif b**2 - 4*a*c == 0 : # 판별식 (근이 2개)
        result.add(x) # 기본 해 x
        result.add(-b / (2*a)) # 나머지 해 (1차 방정식의 해)
    else : # 판별식 (근이 3개)
        result.add(x) # 기본해 x
        result.add((-b+(b**2 - 4*a*c)**(1/2))/(2*a)) # 나머지 해 1 (근의 공식)
        result.add((-b-(b**2 - 4*a*c)**(1/2))/(2*a)) # 나머지 해 2 (근의 공식)
    result = sorted(list(result)) #요구 조건에 따른 오름차순 정렬
    # 밑에는 출력 요구조건
    if len(result) == 3:
        print(f'{result[0]:.4f} {result[1]:.4f} {result[2]:.4f}')
    elif len(result) == 2:
        print(f'{result[0]:.4f} {result[1]:.4f}')
    else :
        print(f'{result[0]:.4f}')  
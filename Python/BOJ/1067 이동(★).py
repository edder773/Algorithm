p = 998244353 # 적당히 큰 소수
def fft(a, inverse): # 리스트를 입력받아 수행(True면 FFT의 역변환, False면 FFT를 통한 DFT)
    n = len(a)
    j = 0
    for i in range(1,n): # 입력 신호의 시간축 정보를 뒤집어서 변환
        reverse = n // 2
        while j >= reverse:
            j -= reverse
            reverse //= 2
        j += reverse
        if i < j:
            a[i], a[j] = a[j], a[i]
    # Cooley-Tukey 알고리즘
    step = 2
    while step <= n: 
        half = step // 2 # 현재 단계 절반
        u = pow(2, p//step, p) # 실수 곱셈의 단위 원소로 대체
        if inverse: # 역변환을 수행해야 할 경우
            u = pow(u, p-2,p) # 역원을 구해야 하므로 u^p-2 % p
        for i in range(0, n, step):
            w = 1
            for j in range(i, i + half):
                v = a[j + half] * w
                a[j + half] = (a[j] - v)% p
                a[j] = (a[j]+v) % p
                w = (u*w) % p
        step *= 2

    if inverse:  # 역변환 수행시 변환 과정
        num = p - (p-1) // n
        for i in range(n):
            a[i] = (a[i] * num) %p

def convergence(a, b):
    x = len(a) + len(b) - 1 # 두 다항식의 곱으로 최대 다항식 x
    n = 1 << x.bit_length()
    # 리스트의 크기를 2의 제곱수로 맞춰 주기 위해 0으로 처리
    a += [0 for _ in range(n - len(a))]
    b += [0 for _ in range(n - len(b))]
    # 시간축으로 변환 진행
    fft(a,False) 
    fft(b,False)
    for i in range(n):
        a[i] *= b[i] # convergence 계산
    fft(a,True) # 다시 역변환 해서 값을 얻음
    return a

import sys
n = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().split()))
y = list(map(int, sys.stdin.readline().split()))
y.reverse() # 뒤집어서 계산(정확도)
result = convergence(x+x,y)
print(max(result))
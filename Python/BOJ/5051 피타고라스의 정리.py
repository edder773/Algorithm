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
        u = pow(3, p//step, p) # 3의 제곱 수
        if inverse: # 역변환을 수행해야 할 경우
            u = pow(u, p-2,p) # u의 p-2제곱으로 처리
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

def square(arr):
    # n = (1 << len(arr).bit_length())*2
    n = 2
    while n < len(arr):
        n *= 2
    n *= 2
    # print(n,m)
    # 리스트의 크기를 2의 제곱수로 맞춰 주기 위해 0으로 처리
    arr += [0 for _ in range(n - len(arr))]
    fft(arr, False)
    # 피타고라스는 각 변의 제곱으로 리스트를 구함
    arr_square = [(i**2) % p for i in arr]
    fft(arr_square, True)
    return arr_square

import sys
n = int(sys.stdin.readline())
a = [0]*n
result = 0
for i in range(1, n):
    a[(i**2) % n] += 1
b = square(a[:])

# a[i] * b[i] = c^2인 경우의 수
# a[i] * b[i+n] = c^2인 경우의 수 // 푸리에 함수의 주기성 규칙
# a[i] * a[i*2 % n] => a와 b 중 작은 값을 2배한 값이 c보다 작을 떄의 경우의 수
for i in range(n):
    result += (a[i] * b[i]) + (a[i] * b[i + n]) + (a[i] * a[i*2 % n]) 
    
print(result // 2)
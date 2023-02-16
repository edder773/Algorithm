def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return a*b // gcd(a, b)


N = int(input())
x = list(map(int, input().split()))
for i in range(N-1):
    print(f'{lcm(x[0],x[i+1])//x[i+1]}/{lcm(x[0],x[i+1])//x[0]}')

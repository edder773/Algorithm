def cursives(n):
    for i in range(2, n):
        x = 0
        if n % i == 0:
            print(i)
            return (cursives(n//i))
    if n == 1:
        return ''
    return n


N = int(input())
print(cursives(N))

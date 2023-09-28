def decomposite(n):
    if n == 1:
        return [2, '나', 2]
    if n < 10:
        return [n]
    for i in range(9, 1, -1):
        if n % i == 0:
            return decomposite(n // i) + ['따', i]
    cand = -1
    maxdiv = -1
    for i in range(2, 10):
        for j in range(2, 10):
            if (n - i) % j == 0 and j > maxdiv:
                maxdiv = j
                cand = i
                break
    return decomposite(n - cand) + ['다', cand]
 
def each(n):
    name = ['', '', '박', '받', '밤', '발', '밦', '밝', '밣', '밞']
    arr = decomposite(n)
    string = ''
    for i in range(len(arr) - 1, -1, -2):
        string += name[arr[i]]
    for i in range(1, len(arr), 2):
        string += arr[i]
    string += '맣'
    return string
 
def aheui(string):
    ret = ''
    for i in string:
        ret += each(ord(i))
    return ret + '희'
 
aheui('''임나연''')
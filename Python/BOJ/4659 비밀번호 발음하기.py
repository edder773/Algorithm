import sys

vowel = ['a','e','i','o','u']

while True:
    password = sys.stdin.readline().strip()
    check = True
    checknum = 0
    if password == 'end':
        break

    for i in vowel:
        if i in password:
            break
    else:
        check = False
    
    vt, ct = 0,0
    for i in password:
        if i in vowel :
            vt += 1
            ct = 0
        else :
            vt = 0
            ct += 1

        if vt == 3 or ct == 3:
            check = False
            break

    for i in range(len(password)-1):
        if password[i] == password[i+1] and password[i] != 'e' and password[i] != 'o':
            check = False
            break
    
    if check:
        print(f'<{password}> is acceptable.')
    else:
        print(f'<{password}> is not acceptable.')
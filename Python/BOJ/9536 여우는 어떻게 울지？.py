import sys
T = int(sys.stdin.readline())
for _ in range(T):
    sound = list(sys.stdin.readline().strip().split())
    noise = []
    result = []
    while True:
        S = sys.stdin.readline().strip()
        if S == 'what does the fox say?':
            break
        S = list(S.split())
        for i in range(len(S)):
            if S[i] == 'goes':
                noise.append(S[i+1])
                break
    for i in sound :
        if i not in noise:
            result.append(i)
    print(*result)
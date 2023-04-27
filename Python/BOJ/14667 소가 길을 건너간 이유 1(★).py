# 답 1
import sys
N = int(sys.stdin.readline())
cows = [2]*11
result = 0
for _ in range(N):
    cow, pasture = map(int,sys.stdin.readline().split())
    if cows[cow] == 2: # 소 없으면
        cows[cow] = pasture # 배정
    elif cows[cow] != pasture: # 소는 있는데 다른 목초지면
        cows[cow] = pasture # 그 목초지로 이동하고
        result += 1 # 움직임 증가
print(result)

# 답 2
import sys
N = int(sys.stdin.readline())
cows = [[],[]]
result = 0
for _ in range(N):
    cow, move = map(int, sys.stdin.readline().split())
    if cow not in cows[0] and cow not in cows[1]:
        cows[move].append(cow)
    else :
        if cow not in cows[move]:
            if move == 0 :
                cows[1].remove(cow)
                cows[0].append(cow)
            else :
                cows[0].remove(cow)
                cows[1].append(cow)
            result += 1
print(result)
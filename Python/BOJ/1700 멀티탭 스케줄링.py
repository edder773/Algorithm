import sys
N, K = map(int, sys.stdin.readline().split())
items = list(map(int, sys.stdin.readline().split()))
plugs = []
result = 0
for i in range(K):
    if items[i] not in plugs:
        if len(plugs) < N:
            plugs.append(items[i])
        else :
            temp2 = 0
            temp = 0
            for plug in plugs:
                if plug not in items[i:]:
                    temp = plug
                    break
                elif items[i:].index(plug) > temp2:
                    temp2 = items[i:].index(plug)
                    temp = plug
            plugs[plugs.index(temp)] = items[i]
            result += 1
print(result)
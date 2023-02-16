T = int(input())
for case in range(1, T+1):
    N = input()
    out = ''
    inner = ''
    middle = ''
    for i in N:
        out += '..#.'  # 맨위 or 아랫줄에 ..#. 추가
        inner += '.#.#'  # 그아래 or 그윗줄에 .#.# 추가
        middle += '#.' + i + '.'  # 가운데 줄에# N요소 . 추가
    out += '.'  # 마지막 밖에 .추가
    inner += '.'  # 마지막 안에 . 추가
    middle += '#'  # 마지막에 # 추가
    print(out, inner, middle, inner, out, sep='\n')

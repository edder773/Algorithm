table = [[0]*30 for _ in range(30)]

for i in range(15):
    table[15][14-i] = 1
    table[14-i][15] = 1*16
    table[15][15+i] = 1*16*16
    table[15+i][15] = 1*16*16*15
    table[15][15] = 0

for result in table:
    print(*result)
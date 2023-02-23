bingo = [list(map(int, input().split())) for _ in range(5)]
num = [list(map(int, input().split())) for _ in range(5)]
cnt = 0
for i in range(5):
    for j in range(5):
        cnt_bingo = 0
        for a in range(5):
            for b in range(5):
                if num[i][j] == bingo[a][b]:
                    cnt += 1
                    bingo[a][b] = 0
                    bingo_across1 = [bingo[i][4-i] for i in range(5)]
                    bingo_across2 = [bingo[i][i] for i in range(5)]
                    bingo_cross = [[0]*5 for _ in range(5)]
                    for s in range(5):
                        for t in range(5):
                            bingo_cross[s][t] = bingo[t][s]
                    break
            if num[i][j] == bingo[a][b]:
                break
        if sum(bingo_across1) == 0:
            cnt_bingo += 1
        if sum(bingo_across2) == 0:
            cnt_bingo += 1
        for k in range(5):
            if sum(bingo[k]) == 0:
                cnt_bingo += 1
            if sum(bingo_cross[k]) == 0:
                cnt_bingo += 1
        if cnt_bingo >= 3:
            break
    if cnt_bingo >= 3:
        break
print(cnt)
import sys
N = int(sys.stdin.readline())
cookie = [list(sys.stdin.readline().strip()) for _ in range(N)]

heart_x, heart_y = 0, 0
arm_left, arm_right = 0, 0
back = 0
leg_left, leg_right = 0, 0
for i in range(N):
    for j in range(N):
        if cookie[i][j] == '*':
            if not heart_x and not heart_y:
                heart_x, heart_y = i+1, j
            elif heart_x == i and heart_y > j:
                arm_left += 1
            elif heart_x == i and heart_y < j:
                arm_right += 1
            elif heart_x < i and heart_y == j:
                back += 1
            elif heart_x + back < i and heart_y > j:
                leg_left += 1
            elif heart_x + back < i and heart_y < j:
                leg_right += 1

print(heart_x+1, heart_y+1)
print(arm_left,arm_right, back, leg_left,leg_right)
            
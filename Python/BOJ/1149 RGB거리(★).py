# 입력조건
import sys
N = int(sys.stdin.readline())
RGB = [0]*N
for x in range(N):
    RGB[x] = list(map(int, sys.stdin.readline().split()))

for i in range(1, N):
    # 다음 RGB의 각 인덱스에 대해 이전값 중의 해당 값 제외한 RGB 중의 최솟값을 + (경우의수를 따짐)
    RGB[i][0] = min(RGB[i-1][1], RGB[i-1][2])+RGB[i][0]
    RGB[i][1] = min(RGB[i-1][0], RGB[i-1][2])+RGB[i][1]
    RGB[i][2] = min(RGB[i-1][0], RGB[i-1][1])+RGB[i][2]
print(min(RGB[N-1]))

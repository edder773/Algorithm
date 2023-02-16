T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    floor_H = str(N % H)
    if (floor_H == "0"):
        floor_H = str(H)
    floor_W = str(N//H + 1).zfill(2)
    if (N % H == 0):
        floor_W = str(N//H).zfill(2)
    print(floor_H+floor_W)

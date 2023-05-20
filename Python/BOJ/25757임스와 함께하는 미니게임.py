import sys
N, game = sys.stdin.readline().split()
player = set()
for _ in range(int(N)):
    player.add(sys.stdin.readline().strip())
if game == 'Y':
    print(len(player))
elif game == 'F':
    print(len(player)//2)
elif game == 'O':
    print(len(player)//3)
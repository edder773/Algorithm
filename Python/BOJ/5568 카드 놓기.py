import sys
from itertools import permutations
n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
cards = list(sys.stdin.readline().strip() for _ in range(n))
result = set()
for card in permutations(cards,k):
    num = ''
    for i in card:
        num += i
    result.add(num)
print(len(result))
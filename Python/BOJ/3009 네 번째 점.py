temp_x = []
temp_y = []
for i in range(3):
    n, m = map(int, input().split())
    temp_x.append(n)
    temp_y.append(m)
if temp_x.count(min(temp_x)) == 2:
    print(max(temp_x), end=' ')
elif temp_x.count(max(temp_x)) == 2:
    print(min(temp_x), end=' ')

if temp_y.count(min(temp_y)) == 2:
    print(max(temp_y), end=' ')
elif temp_y.count(max(temp_y)) == 2:
    print(min(temp_y), end=' ')

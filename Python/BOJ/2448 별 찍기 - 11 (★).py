# 방법 1
def star(n):
    if n == 3:
        return ['  *  ',' * * ','*****']
    stars = star(n//2)
    x = [' ' * (n//2) + i + ' ' * (n//2) for i in stars] # 머리부분 삼각형
    y = [i + ' ' + i for i in stars] # 몸부분 삼각형 3개 영역
    return x+y
import sys
N = int(sys.stdin.readline())
result = star(N)
print('\n'.join(result))

# 방법 2
def stars(y, x, n):
    if n == 3:
        # 첫번째 줄 3번째 칸(한가운데(N-1)) = *
        star[y][x] = '*' 
        # 두번째 줄 2번째, 4번째 칸 = * (가운데 뚫린 별)
        star[y+1][x-1] = '*'  
        star[y+1][x+1] = '*' 
        # 세번째 줄 5개의 *로 채우기
        star[y+2][x-2] ='*'
        star[y+2][x-1] ='*'
        star[y+2][x] ='*'
        star[y+2][x+1] ='*'
        star[y+2][x+2] ='*'
    else :
        stars(y, x, n//2) 
        stars(y + n//2 , x + n//2 , n//2) # 오른쪽 모양
        stars(y + n//2 , x - n//2 , n//2) # 왼쪽 모양
        
import sys
N = int(sys.stdin.readline())
# 예제 마지막줄보면 ***** ***** ***** ... 로 별 5칸+ 공백 1칸으로 6칸 * 8개로 지정 -> 2*N개의 공백
star = [[' '] * (2*N) for _ in range(N)]
stars(0,N-1,N)

for i in star:
    print(''.join(i))
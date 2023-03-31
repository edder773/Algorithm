# 백트래킹을 이용한 방법
def find(a,pay):
    global result
    if pay >= result:
        return
    if a >= 12:
        result = min(result,pay)
    else :
        find(a+1, pay+plan[a]*d) # 1일권
        find(a+1, pay+m) # 한달권
        find(a+3, pay+m3) # 3달권
        find(a+12, pay+y) # 1년권


T = int(input())
for case in range(1,T+1):
    d, m, m3, y = map(int,input().split())
    plan = list(map(int, input().split()))
    result = float('inf')
    find(0,0)
    print(f'#{case} {result}')

# # 다이나믹 프로그래밍을 이용한 방법
# T = int(input())
# for case in range(1, T + 1):
#     d, m, m3, y = map(int, input().split())
#     plan = list(map(int, input().split()))
#     x = [0]*12
#     x[0] = min(plan[0]*d, m, m3, y)
#     x[1] = min(x[0] + plan[1]*d, x[0] + m, m3, y)
#     x[2] = min(x[1] + plan[2]*d, x[1] + m, m3, y)
#     for i in range(3,12):
#         x[i] = min(x[i-1] + plan[i]*d, x[i-1] + m, x[i-3] + m3, y)
#     print(f'#{case} {x[11]}')

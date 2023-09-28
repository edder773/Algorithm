import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
result = [0]
for i in A: # 각 값에 대해
    if result[-1] < i: # 끝값보다 크면
        result.append(i) # 집어 넣고

    else: # 작으면
        left, right = 0, len(result)  #이분 탐색을 해보자
        while left < right:
            mid = (left + right)//2
            if result[mid] < i:
                left = mid + 1
            else :
                right = mid
        result[right] = i
print(len(result)-1)
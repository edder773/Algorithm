import sys	
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

not_sort_arr = {} # 정렬하기 전 각 숫자들의 현재 인덱스를 저장
for i in range(N):
    not_sort_arr[arr[i]] = i

arr.sort()
sort_arr = {} #정렬 후 각 숫자들의 현재 인덱스를 저장
for j in range(N):
    sort_arr[arr[j]] = j

result = 0
for k in arr:
    result = max(result, not_sort_arr[k] - sort_arr[k]) # 정렬 전과 후의 인덱스 차이 중 가장 큰 애가 찾는 값

print(result)
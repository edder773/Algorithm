import sys
k,n = map (int, sys.stdin.readline().split())
check = [0]
find = set() # a = 0, b = 1 일때 항상 0, 1 ,k란 해를 만족하므로
find.add((0,1,k))

while n:
  temp = find.copy() # 현재 find를 temp에 복사
  for a, b, c in find: # 찾아보자
    if a != b and b != c: # 둘이 서로 수 이므로
      if a not in check and b not in check and c not in check: # 이미 나온 값도 아니면
        check += [a,b,c] # 나중에 빼야하니 체크
        print(a,b,c) # 이 때의 a,b,c 출력
        n -= 1 # 1씩 줄여가보자
        if n == 0: # n이 0이 되면
          break #끝내!
      for _ in range(3): # 3번의 반복 (a,b,c 각각에 대해 미분해보자)
        x = k * (a + b) - c # 미분 했을때 정점 (a,b,c 순서대로)
        if x >= 0: # 만약 정점이 0보다 크면
          temp.add(tuple(sorted([a,b,x]))) # 임시 값에 저장해
        a, b, c = b, c, a # 다른 3점 정점 찾아보자
  find = temp # find 갱신
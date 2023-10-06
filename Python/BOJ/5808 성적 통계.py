import sys
K = int(sys.stdin.readline())
for i in range(1,K+1):
    N, *students = map(int, sys.stdin.readline().split())
    students.sort()
    result = 0
    for j in range(N-1):
        result = max(result, students[j+1] - students[j])
    print(f'Class {i}')
    print(f'Max {students[-1]}, Min {students[0]}, Largest gap {result}')
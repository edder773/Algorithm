import sys
result = 0
credit = 0
sco = {'A+':4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}
for _ in range(20):
    subject, score, grade = sys.stdin.readline().split()
    if grade != 'P':
        credit += float(score)
        result += float(score)*float(sco[grade])
print(round(result/credit,6))
import sys
N = int(sys.stdin.readline())
result ="No Answer"
for i in range(10000,100000):
    x, y = str(i), str(N-i)
    # y의 자리수가 5자리수여야하고, l 부분도 같아야하며, o 부분도 같고, 중복이 없다면
    if len(y) == 5 and x[2]==x[3]==y[3] and x[4]==y[1] and len(set(x+y))==7:
        result =f"  {x}\n+ {y}\n-------\n {N:6}"
        break
print(result)

# import sys
# N = int(sys.stdin.readline())
# for d in range(10):
#     for e in range(10):
#         for h in range(1,10):
#             for l in range(10):
#                 for o in range(10):
#                     for r in range(10):
#                         for w in range(1,10):
#                             if d != e and d != h and d != l and d != o and d!= r and d != w:
#                                 if e != h and e != l and e != o and e != r and e!=w :
#                                     if h != l and h != o and h != r and h!= w :
#                                         if l != o and l != r and l != w:
#                                             if o != r and o!= w:
#                                                 if r != w:
#                                                     x = str(h)+str(e)+str(l)+str(l)+str(o)
#                                                     y = str(w)+str(o)+str(r)+str(l)+str(d)
#                                                     if int(x)+int(y) == N:
#                                                         print(' ',x)
#                                                         print('+',y)
#                                                         print('-------')
#                                                         print(f" {N:6}")
#                                                         exit()
# print('No Answer')
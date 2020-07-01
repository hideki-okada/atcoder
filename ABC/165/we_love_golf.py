K = int(input())
A, B = map(int, input().split())
ok_flag = False
for i in range(A, B + 1):
    if i % K == 0:
        ok_flag = True
        break
if ok_flag:
    print('OK')
else:
    print('NG')

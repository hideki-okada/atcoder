N = int(input())
a = [list(input()) for _ in range(N)]
ans = ''
not_flag = 0
for i in range(N // 2):
    rel1 = list(set(a[i]))
    rel2 = list(set(a[-1 - i]))
    flag = 0
    for s in rel1:
        if s in rel2:
            ans += s
            flag = 1
            break
    if not flag:
        not_flag = 1
        break
if not_flag:
    print(-1)
else:
    if N % 2 == 0:
        print(ans + ''.join(list(reversed(ans))))
    else:
        print(ans + a[N//2][0] + ''.join(list(reversed(ans))))

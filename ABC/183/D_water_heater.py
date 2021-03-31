N, W = map(int, input().split())
s_t_p = [list(map(int, input().split())) for _ in range(N)]
flag = True
L = [0 for _ in range(2 * 10 ** 5 + 1)]
for i, (s, t, p) in enumerate(s_t_p):
    L[s] += p
    L[t] -= p
for i in range(2 * 10 ** 5 + 1):
    if i > 0:
        L[i] += L[i - 1]
    if L[i] > W:
        print('No')
        flag = False
        break
if flag:
    print('Yes')

import numpy as np

N, M, X = map(int, input().split())
c = []
a = []
for i in range(N):
    tmp = list(map(int, input().split()))
    c.append(tmp[0])
    a.append(tmp[1:])
c = np.array(c)
a = np.array(a)
min_money = 10 ** 8
flag = False
for i in range(2 ** N):
    order = []
    for j in range(N):
        if (i >> j) & 1:
            order.append(j)
    if not len(order):
        continue
    rikaido = np.sum(a[np.array(order)], axis=0)
    if np.all(rikaido >= X):
        flag = True
        money = np.sum(c[order])
        if min_money > money:
            min_money = money
if flag:
    print(min_money)
else:
    print(-1)

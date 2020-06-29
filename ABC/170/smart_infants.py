from heapq import heappush, heappop, heapify
from sys import stdin

max_class_num = 2 * 10 ** 5

readline = stdin.readline
N, Q = map(int, input().split())
ab = [list(map(int, readline().split())) for _ in [0] * N]
cd = [list(map(int, readline().split())) for _ in [0] * Q]
enji_rate = [0] * (N + 1)
enji_cls = [0] * (N + 1)
cls_rate = [[] for _ in range(max_class_num + 1)]
for i, (a, b) in enumerate(ab):
    enji_rate[i] = a
    enji_cls[i] = b
    heappush(cls_rate[b], (-a, i))


def max_rate_in_cls(c):
    q = cls_rate[c]
    while q:
        x, enj = q[0]
        if enji_cls[enj] == c:
            return -x
        else:
            heappop(q)
    return 0


max_rate = []
for c in range(max_class_num + 1):
    x = max_rate_in_cls(c)
    if x:
        max_rate.append((x, c))
heapify(max_rate)


def get_ans():
    q = max_rate
    while True:
        x, c = q[0]
        if max_rate_in_cls(c) == x:
            return x
        heappop(q)


for enj, after_cls in cd:
    before_cls = enji_cls[enj]
    heappush(cls_rate[after_cls], (-enji_rate[enj], enj))
    enji_cls[enj] = after_cls
    for c in (before_cls, after_cls):
        x = max_rate_in_cls(c)
        if x != 0:
            heappush(max_rate, (x, c))
    print(max_rate)
    print(get_ans())

import itertools

import numpy as np

N = int(input())
a = [list(map(int, input().split())) for _ in range(N)]

max_len = 0
for v in itertools.combinations(range(N), 2):
    tmp_len = np.linalg.norm(np.array(a[v[0]]) - np.array(a[v[1]]))
    if max_len < tmp_len:
        max_len = tmp_len
print(max_len)
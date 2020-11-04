import math
import itertools
import numpy as np
from scipy.sparse.csgraph import connected_components
from collections import Counter

mod = 998244353
N, K = map(int, input().split())
a = [list(map(int, input().split())) for i in range(N)]
columns_swap_matrix = [[0 for i in range(N)] for i in range(N)]
rows_swap_matrix = [[0 for i in range(N)] for i in range(N)]
index_list = [i for i in range(N)]
for v in itertools.combinations(index_list, 2):
    # columnsについて
    for i in range(N):
        if a[i][v[0]] + a[i][v[1]] > K:
            break
        if i == N - 1:
            columns_swap_matrix[v[0]][v[1]] = 1
            columns_swap_matrix[v[1]][v[0]] = 1
    for i in range(N):
        # rowsについて
        if a[v[0]][i] + a[v[1]][i] > K:
            break
        if i == N - 1:
            rows_swap_matrix[v[0]][v[1]] = 1
            rows_swap_matrix[v[1]][v[0]] = 1

n, labels = connected_components(np.array(columns_swap_matrix))
columns_baai = 1
for k, v in Counter(labels).items():
    columns_baai *= math.factorial(v)
columns_baai %= mod
n, labels = connected_components(np.array(rows_swap_matrix))
rows_baai = 1
for k, v in Counter(labels).items():
    rows_baai *= math.factorial(v)
rows_baai %= mod
ans = columns_baai * rows_baai
ans %= mod
print(ans)
import numpy as np


def search_neighbor(arr, idx):
    ans = []
    for lin in np.where(arr == idx)[0]:
        ans.append(int(arr[lin][arr[lin] != idx]))
    return np.array(ans)


N, M, Q = map(int, input().split())
relation = np.array([list(map(int, input().split())) for _ in range(M)])
relation -= 1
c = np.array(list(map(int, input().split())))
s = [list(map(int, input().split())) for _ in range(Q)]

for query in s:
    if len(query) == 2:
        print(c[query[1] - 1])
        neighbor = search_neighbor(relation, query[1] - 1)
        if len(neighbor):
            c[neighbor] = c[query[1] - 1]
    else:
        print(c[query[1] - 1])
        c[query[1] - 1] = query[2]

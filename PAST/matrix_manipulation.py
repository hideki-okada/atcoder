import sys
from copy import deepcopy

import numpy as np


def main():
    input = sys.stdin.readline
    n = int(input())
    q = int(input())
    s = [list(map(int, input().split())) for _ in range(q)]
    a = np.array([[n * i + j for j in range(n)] for i in range(n)])

    for query in s:
        if query[0] == 1 and query[1] != query[2]:
            tmp = deepcopy(a[query[1] - 1])
            a[query[1] - 1] = a[query[2] - 1]
            a[query[2] - 1] = tmp
        elif query[0] == 2 and query[1] != query[2]:
            tmp = deepcopy(a[:, query[1] - 1])
            a[:, query[1] - 1] = a[:, query[2] - 1]
            a[:, query[2] - 1] = tmp
        elif query[0] == 3:
            a = a.T
        elif query[0] == 4:
            print(a[query[1] - 1, query[2] - 1])


if __name__ == '__main__':
    main()

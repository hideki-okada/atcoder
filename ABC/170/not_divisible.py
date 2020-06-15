import numpy as np
from sys import stdin

def main():
    readline = stdin.readline
    N = int(readline())
    a = list(map(int, readline().split()))
    a = np.sort(a)
    count = 0
    idxes = np.arange(len(a))
    while len(idxes):
        idx = idxes[0]
        idxes = np.delete(idxes, 0)
        var = a[idx]
        if len(np.where(a[idxes] == var)[0]) == 0:
            count += 1
        idxes = idxes[np.where(a[idxes] % var != 0)[0]]
    print(count)

main()
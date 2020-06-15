import numpy as np
from sys import stdin

def detect_equality(a):
    idx_list = set(a[:, 1])
    return np.min([np.max(a[a[:, 1] == n][:, 0]) for n in idx_list])

def main():
    readline = stdin.readline
    N, Q = map(int, input().split())
    a = [list(map(int, readline().split())) for _ in [0] * N]
    c = [list(map(int, readline().split())) for _ in [0] * Q]
    a = np.array(a)
    for youji_idx, youchien_idx in c:
        a[youji_idx - 1, 1] = youchien_idx
        print(detect_equality(a))

main()
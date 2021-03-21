from copy import deepcopy

import numpy as np

H, W, A, B = map(int, input().split())
masu = np.array([[0] * W] * H)
count = 0
masume_rireki = [[] for i in range(A)]


def umetate(masume, nokorimaisuu_a, nokorimaisuu_b):
    global count
    global masume_rireki
    if nokorimaisuu_a == 0:
        count += 1
    elif nokorimaisuu_a > 0:
        for i in range(H):
            for j in range(W):
                masume_pattern = deepcopy(masume)
                if j + 1 < W and masume_pattern[i, j] == 0 and masume_pattern[i, j + 1] == 0:
                    masume_pattern[i, j] = 1
                    masume_pattern[i, j + 1] = 1
                    if masume_pattern.flatten().tolist() in masume_rireki[A-nokorimaisuu_a]:
                        continue
                    else:
                        masume_rireki[A-nokorimaisuu_a].append(masume_pattern.flatten().tolist())
                        umetate(masume_pattern, nokorimaisuu_a - 1, nokorimaisuu_b)
                masume_pattern = deepcopy(masume)
                if i + 1 < H and masume_pattern[i, j] == 0 and masume_pattern[i + 1, j] == 0:
                    masume_pattern[i, j] = -1
                    masume_pattern[i + 1, j] = -1
                    if masume_pattern.flatten().tolist() in masume_rireki[A-nokorimaisuu_a]:
                        continue
                    else:
                        masume_rireki[A-nokorimaisuu_a].append(masume_pattern.flatten().tolist())
                        umetate(masume_pattern, nokorimaisuu_a - 1, nokorimaisuu_b)


def fact(x):
    if x == 0:
        return 1
    else:
        return x * fact(x - 1)


if A == 0:
    print(1)
else:
    umetate(masu, A, B)
    print(count)

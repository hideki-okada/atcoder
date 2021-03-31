from typing import List

import numpy as np
from scipy.sparse.csgraph import connected_components

N, K = map(int, input().split())
P = list(map(int, input().split()))
C = list(map(int, input().split()))


def make_adjacency_matrix(input_list: List[int]):
    adjacency_matrix = [[0] * N for _ in range(N)]
    for i, v in enumerate(input_list):
        adjacency_matrix[i][v - 1] = 1
    return adjacency_matrix


def detect_one_roop_max_score(C, P, K, idx_array):
    max_score = -10 ** 10
    for idx in idx_array:
        _max_score = -10 ** 10
        sum = 0
        cur_idx = idx
        count = 0
        while True:
            if P[cur_idx] - 1 == idx:
                break
            if count >= K:
                break
            sum += C[P[cur_idx] - 1]
            if _max_score < sum:
                _max_score = sum
            cur_idx = P[cur_idx] - 1
            count += 1
        if max_score < _max_score:
            max_score = _max_score
    return max_score


adjacency_matrix = make_adjacency_matrix(P)
n, labels = connected_components(np.array(adjacency_matrix))
score = - 10 ** 10
# ループ毎に最大値を計算し、最も大きいスコアを出力する
for i in range(n):
    idx_array = np.where(labels == i)[0]
    roop_values = np.array(C)[idx_array]
    one_roop_sum = np.sum(roop_values)
    max_value = max(roop_values)
    min_value = min(roop_values)
    if one_roop_sum <= 0:
        tmp_score = detect_one_roop_max_score(C, P, K, idx_array)
    else:
        n_roop = K // len(idx_array)
        one_roop_max_score = detect_one_roop_max_score(C, P, K - n_roop * len(idx_array), idx_array)
        tmp_score = one_roop_sum * n_roop + one_roop_max_score
    if score < tmp_score:
        score = tmp_score
print(score)

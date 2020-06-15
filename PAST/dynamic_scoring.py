import numpy as np

N, M, Q = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(Q)]
score = np.zeros((N, M)).astype(np.int)
score_m = np.ones(M).astype(np.int) * N
for query in s:
    if len(query) == 3:
        if score[query[1] - 1][query[2] - 1] == 1:
            continue
        score_m[query[2] - 1] -= 1
        score[query[1] - 1][query[2] - 1] = 1
    else:
        print(np.dot(score[query[1] - 1], score_m))

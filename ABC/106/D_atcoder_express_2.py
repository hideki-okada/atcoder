import numpy as np

N, M, Q = map(int, input().split())
train_range = [list(map(int, input().split())) for _ in range(M)]
questions = [list(map(int, input().split())) for _ in range(Q)]

train_range = np.array(train_range)
questions = np.array(questions)
for q in questions:
    ans = q[np.newaxis, :] - train_range
    ans = (answers[:, :, 0] <= 0) * (answers[:, :, 1] >= 0)
# ans = np.sum(ans, axis=1)
'''
for a in ans:
    print(a)
'''
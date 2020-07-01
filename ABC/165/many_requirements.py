import itertools

N, M, Q = map(int, input().split())
q = [list(map(int, input().split())) for _ in range(Q)]
a = [0] * N
max_score = 0
for v in itertools.combinations(range(N + M - 1), N):
    tmp_score = 0
    for n in range(N):
        a[n] = v[n] + 1 - n
    for query in q:
        if (a[query[1] - 1] - a[query[0] - 1]) == query[2]:
            tmp_score += query[3]
    if max_score < tmp_score:
        max_score = tmp_score
print(max_score)

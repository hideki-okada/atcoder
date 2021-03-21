N, M, Q = list(map(int, input().split()))
WV = [list(map(int, input().split())) for _ in range(N)]
X = list(map(int, input().split()))
queries = [list(map(int, input().split())) for _ in range(Q)]
WV = sorted(WV, key=lambda x: x[1], reverse=True)

for query in queries:
    l, r = query
    available_box = X[:l - 1] + X[r:]
    available_box = sorted(available_box)
    score = 0
    for w, v in WV:
        for i, box in enumerate(available_box):
            if w <= box:
                available_box.pop(i)
                score += v
                break
    print(score)

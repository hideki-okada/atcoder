H, W, K = map(int, input().split())
c = [list(input()) for _ in range(H)]
erabikata = 0
for i in range(2 ** H):
    if i == 0:
        continue
    ans_h = []
    for ii in range(H):
        if i >> ii & 1:
            ans_h.append(c[ii])
    if ans_h:
        ans_h = [list(x) for x in zip(*ans_h)]
    for j in range(2 ** W):
        ans_all = []
        count = 0
        if j == 0:
            continue
        for jj in range(W):
            if j >> jj & 1:
                ans_all.append(ans_h[jj])
        for v in sum(ans_all, []):
            if v == '#':
                count += 1
        if count == K:
            erabikata += 1
print(erabikata)

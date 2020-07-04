N, M = map(int, input().split())
relation = [[0 for j in range(N + 1)] for i in range(N + 1)]
for i in range(M):
    x, y = map(int, input().split())
    relation[x][y] = 1
max_giin = 0
for i in range(2 ** N):
    habatsu_menber = []
    bad_flag = 0
    for j in range(N):
        if i >> j & 1:
            habatsu_menber.append(j + 1)
    for men_1 in habatsu_menber:
        for men_2 in habatsu_menber:
            if men_1 < men_2 and relation[men_1][men_2] != 1:
                bad_flag = 1
                break
        else:
            continue
        break
    if not bad_flag and max_giin < len(habatsu_menber):
        max_giin = len(habatsu_menber)

print(max_giin)

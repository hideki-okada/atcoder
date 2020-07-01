D, G = map(int, input().split())
pc = [list(map(int, input().split())) for _ in range(D)]
min_solve_num = 1000
for i in range(1, 2 ** D):
    score = 0
    tmp_solve_num = 0
    for j in range(D):
        if (i >> j) & 1:
            score += pc[j][0] * (j + 1) * 100 + pc[j][1]
            tmp_solve_num += pc[j][0]
    if score >= G and tmp_solve_num < min_solve_num:
        min_solve_num = tmp_solve_num
score = 0
tmp_solve_num = 0
for i in range(D - 1, -1, -1):
    num = pc[i][0]
    for j in range(num):
        score += (i + 1) * 100
        tmp_solve_num += 1
        if j == num - 1:
            score += pc[i][1]
        if score >= G:
            break
    else:
        continue
    break
if tmp_solve_num < min_solve_num:
    min_solve_num = tmp_solve_num
print(min_solve_num)

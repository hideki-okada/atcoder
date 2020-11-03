import copy
import sys
from typing import List

sys.setrecursionlimit(1000000)

field = [list(input()) for _ in range(10)]
num_land = 0
# 陸地の数を求める
for l in field:
    for m in l:
        if m == 'o':
            num_land += 1
# 埋め立て分を足す
num_land += 1
seen = [[0 for _ in range(10)] for _ in range(10)]
dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)


def dfs(tmp_field: List[str], tmp_seen: List[int], h: int, w: int):
    tmp_seen[h][w] = 1
    for i in range(4):
        nh = h + dy[i]
        nw = w + dx[i]
        if nh >= 10 or nh < 0 or nw >= 10 or nw < 0:
            continue
        if tmp_field[nh][nw] == 'x':
            continue
        if tmp_seen[nh][nw] == 1:
            continue
        dfs(tmp_field, tmp_seen, nh, nw)


def main():
    flag = False
    for i in range(10):
        for j in range(10):
            if field[i][j] == 'o':
                continue
            else:
                tmp_field = copy.deepcopy(field)
                tmp_field[i][j] = 'o'
                tmp_seen = copy.deepcopy(seen)
                dfs(tmp_field, tmp_seen, i, j)
                if sum(map(sum, tmp_seen)) == num_land:
                    print('YES')
                    flag = True
                    break
        else:
            continue
        break
    if not flag:
        print('NO')


if __name__ == '__main__':
    main()

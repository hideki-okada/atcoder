# 二部グラフ判定＋ツリー上のDFS
# https://drken1215.hatenablog.com/entry/2019/05/19/224500

import sys

sys.setrecursionlimit(1000000)

num_node = int(input())
relation = [[[], []] for i in range(num_node + 1)]
for i in range(num_node - 1):
    u, v, w = map(int, input().split())
    if w % 2 == 0:
        relation[u][0].append(v)
        relation[v][0].append(u)
    else:
        relation[u][1].append(v)
        relation[v][1].append(u)
colors = [None] * (num_node + 1)


def dfs(n: int, c: int):
    colors[n] = c
    # 偶数
    for even_idx in relation[n][0]:
        if colors[even_idx] is not None:
            continue
        else:
            dfs(even_idx, colors[n])
    # 奇数
    for odd_idx in relation[n][1]:
        if colors[odd_idx] is not None:
            continue
        else:
            dfs(odd_idx, 1 - colors[n])


if __name__ == '__main__':
    dfs(1, 0)
    for ans in list(map(int, colors[1:])):
        print(ans)

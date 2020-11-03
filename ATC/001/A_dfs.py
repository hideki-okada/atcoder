import sys

sys.setrecursionlimit(1000000)

H, W = map(int, input().split())
field = [list(input()) for _ in range(H)]
seen = [[0 for _ in range(W)] for _ in range(H)]
dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)


def dfs(h: int, w: int):
    seen[h][w] = 1
    print(h, w)
    for i in range(4):
        nw = w + dx[i]
        nh = h + dy[i]
        if nh < 0 or nh >= H or nw < 0 or nw >= W:
            continue
        if field[nh][nw] == '#':
            continue
        if seen[nh][nw]:
            continue
        dfs(nh, nw)


def main():
    for i in range(H):
        for j in range(W):
            if field[i][j] == 's':
                sh, sw = i, j
            if field[i][j] == 'g':
                gh, gw = i, j
    dfs(sh, sw)
    if seen[gh][gw]:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()

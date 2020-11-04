# pypyなら通る

from collections import deque

if __name__ == '__main__':
    H, W = map(int, input().split())
    grid = [input() for _ in range(H)]
    dist = [[0] * (W + 2) for _ in range(H + 2)]
    queue = deque()
    for i in range(H):
        for j in range(W):
            if grid[i][j] == '#':
                queue.append((i + 1, j + 1))
                dist[i + 1][j + 1] = 0
            else:
                dist[i + 1][j + 1] = -1
    dy = (0, 1, 0, -1)
    dx = (1, 0, -1, 0)
    while queue:
        y, x = queue.popleft()
        d = dist[y][x]
        for i in range(4):
            new_y = y + dy[i]
            new_x = x + dx[i]
            if dist[new_y][new_x] == -1:
                dist[new_y][new_x] = dist[y][x] + 1
                queue.append((new_y, new_x))
    print(d)

from collections import deque

if __name__ == '__main__':
    H, W = map(int, input().split())
    grid = [input() for _ in range(H)]
    dist = [[-1] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if grid[i][j] == 's':
                sy, sx = i, j
                dist[sy][sx] = 0
            if grid[i][j] == 'g':
                gy, gx = i, j
    queue = deque()
    queue.append((sy, sx))
    dy = (0, 1, 0, -1)
    dx = (1, 0, -1, 0)
    while queue:
        y, x = queue.popleft()
        cost = dist[y][x]
        for i in range(4):
            new_y = y + dy[i]
            new_x = x + dx[i]
            if 0 <= new_y < H and 0 <= new_x < W and dist[new_y][new_x] == -1:
                if grid[new_y][new_x] == '#':
                    dist[new_y][new_x] = cost + 1
                    queue.append((new_y, new_x))
                else:
                    dist[new_y][new_x] = cost
                    queue.appendleft((new_y, new_x))
    if dist[gy][gx] <= 2:
        print('YES')
    else:
        print('NO')

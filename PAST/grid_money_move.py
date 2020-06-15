from collections import deque

import numpy as np


def bfs(obstacle, visited, sx, sy, gx, gy):
    queue = deque([[sx, sy]])
    visited[sx, sy] = 0
    while queue:
        x, y = queue.popleft()
        if [x, y] == [gx, gy]:
            return visited[x, y]
        for j, k in ([1, 0], [-1, 0], [0, 1], [0, -1], [-1, 1], [1, 1]):
            new_x, new_y = x + j, y + k
            if new_x < 0 or new_y < 0:
                continue
            if new_x >= np.shape(visited)[0] or new_y >= np.shape(visited)[1]:
                continue
            if [new_x, new_y] not in obstacle.tolist() and visited[new_x, new_y] == -1:
                visited[new_x, new_y] = visited[x, y] + 1
                queue.append([new_x, new_y])


if __name__ == '__main__':
    N, X, Y = map(int, input().split())
    obstacle = np.array([list(map(int, input().split())) for _ in range(N)])
    obstacle += 201
    sx, sy = 201, 201
    X += 201
    Y += 201
    visited = np.ones((403, 403)).astype(np.int) * -1
    ans = bfs(obstacle, visited, sx, sy, X, Y)
    if ans is None:
        print(-1)
    else:
        print(ans)

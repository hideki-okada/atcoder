from collections import deque, Counter


def bfs(maze, visited, sy, sx, gy, gx):
    queue = deque([[sy, sx]])
    visited[sy][sx] = 0
    dy = (0, 1, 0, -1)
    dx = (1, 0, -1, 0)
    while queue:
        cur_y, cur_x = queue.popleft()
        if [cur_y, cur_x] == [gy, gx]:
            return visited[gy][gx]
        for i in range(4):
            new_y = cur_y + dy[i]
            new_x = cur_x + dx[i]
            if new_x < 0 or new_x >= W or new_y < 0 or new_y >= H:
                continue
            elif visited[new_y][new_x] != -1:
                continue
            elif maze[new_y][new_x] == '#':
                continue
            elif maze[new_y][new_x] == '.':
                visited[new_y][new_x] = visited[cur_y][cur_x] + 1
                queue.append([new_y, new_x])
            else:
                raise ValueError('arienaiyo')


if __name__ == '__main__':
    H, W = map(int, input().split())
    maze = [input() for _ in range(H)]
    visited = [[-1] * W for _ in range(H)]
    sy, sx = 0, 0
    gy, gx = H - 1, W - 1
    min_times = bfs(maze, visited, sy, sx, gy, gx)
    if min_times is None:
        print(-1)
    else:
        num_black = sum([Counter(maze_row)['#'] for maze_row in maze])
        ans = H * W - 2 - (min_times - 1) - num_black
        print(ans)

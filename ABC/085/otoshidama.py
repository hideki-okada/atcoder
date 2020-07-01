N, Y = map(int, input().split())
for x in range(N + 1):
    for y in range(N + 1):
        if (N - x - y >= 0) and (10000 * x + 5000 * y + 1000 * (N - x - y) == Y):
            print(x, y, N - x - y)
            break
    else:
        if x == N and y == N:
            print(-1, -1, -1)
        continue
    break


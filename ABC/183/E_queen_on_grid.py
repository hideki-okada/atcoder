# 累積和とDPで解く問題
H, W = map(int, input().split())
grid = [input() for _ in range(H)]
count = 0
DP = [[-1] * W for _ in range(H)]
X = [[-1] * W for _ in range(H)]
Y = [[-1] * W for _ in range(H)]
Z = [[-1] * W for _ in range(H)]
DP[0][0] = 1
X[0][0] = 0
Y[0][0] = 0
Z[0][0] = 0

for i in range(H):
    for j in range(W):
        if i == 0 and j == 0:
            continue
        X[i][j] = X[i][j - 1] + DP[i][j - 1] if j - 1 >= 0 and grid[i][j] != '#' else 0
        Y[i][j] = Y[i - 1][j] + DP[i - 1][j] if i - 1 >= 0 and grid[i][j] != '#' else 0
        Z[i][j] = Z[i - 1][j - 1] + DP[i - 1][j - 1] if i - 1 >= 0 and j - 1 >= 0 and grid[i][j] != '#' else 0
        DP[i][j] = X[i][j] + Y[i][j] + Z[i][j]
print(DP[H - 1][W - 1])

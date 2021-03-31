H, W, X, Y = map(int, input().split())
S = [list(input()) for _ in range(H)]
count = 1
X_low_flag = True
X_high_flag = True
Y_low_flag = True
Y_high_flag = True
for i in range(1, 100):
    if X_high_flag and X - 1 + i < H and S[X - 1 + i][Y - 1] == '.':
        count += 1
    else:
        X_high_flag = False
    if X_low_flag and X - 1 - i >= 0 and S[X - 1 - i][Y - 1] == '.':
        count += 1
    else:
        X_low_flag = False
    if Y_high_flag and Y - 1 + i < W and S[X - 1][Y - 1 + i] == '.':
        count += 1
    else:
        Y_high_flag = False
    if Y_low_flag and Y - 1 - i >= 0 and S[X - 1][Y - 1 - i] == '.':
        count += 1
    else:
        Y_low_flag = False
print(count)

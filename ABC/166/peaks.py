N, M = map(int, input().split())
H = list(map(int, input().split()))
good_tenboudai = [1] * N
for _ in range(M):
    a, b = map(int, input().split())
    if H[a - 1] < H[b - 1]:
        good_tenboudai[a - 1] = 0
    elif H[a - 1] > H[b - 1]:
        good_tenboudai[b - 1] = 0
    else:
        good_tenboudai[b - 1] = 0
        good_tenboudai[a - 1] = 0
print(sum(good_tenboudai))

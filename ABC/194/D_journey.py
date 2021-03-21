N = int(input())
ans = 0
for i in range(N - 1, 10 ** 5):
    base = pow(N, i)
    keisuu = (N - 1) * (pow(N - 1, i - 1) - 1) if N != 2 else 1
    if base > keisuu * (10 ** 18):
        break
    ans += i * keisuu / base
print(ans)

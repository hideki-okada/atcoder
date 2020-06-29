N = int(input())

ans = 0
for i in range(1, N + 1):
    p = N // i
    ans += (p * (p + 1) * i) // 2
print(ans)
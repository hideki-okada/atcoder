N, K = map(int, input().split())

# a+b, c+dをそれぞれ考える
if K < 0:
    K = -K
ans = 0
for i in range(2 * N - K - 1):
    a_plus_b = i + 2 + K
    c_plus_d = i + 2
    if a_plus_b - 2 > N - 1:
        a_plus_b_baai = 2 * N + 1 - a_plus_b
    else:
        a_plus_b_baai = a_plus_b - 1
    if c_plus_d - 2 > N - 1:
        c_plus_d_baai = 2 * N + 1 - c_plus_d
    else:
        c_plus_d_baai = c_plus_d - 1
    ans += a_plus_b_baai * c_plus_d_baai

print(ans)

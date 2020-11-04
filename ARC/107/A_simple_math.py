mod = 998244353
A, B, C = map(int, input().split())
sum_a = (1 + A) * A // 2
sum_b = (1 + B) * B // 2
sum_c = (1 + C) * C // 2
ans = (((sum_a % mod) * (sum_b % mod)) % mod) * (sum_c % mod)
ans = ans % mod
print(ans)
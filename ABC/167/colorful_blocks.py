import sys

import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N, M, K = map(int, input().split())
mod = 998244353


def fact_table(N, MOD):
    inv = np.empty(N, np.int64)
    inv[0] = 0
    inv[1] = 1
    for n in range(2, N):
        q, r = divmod(MOD, n)
        inv[n] = inv[r] * (-q) % MOD
    fact = np.empty(N, np.int64)
    fact[0] = 1
    for n in range(1, N):
        fact[n] = n * fact[n - 1] % MOD
    fact_inv = np.empty(N, np.int64)
    fact_inv[0] = 1
    for n in range(1, N):
        fact_inv[n] = fact_inv[n - 1] * inv[n] % MOD
    return fact, fact_inv, inv


def main(N, M, K):
    if N == 1:
        return M
    fact, fact_inv, inv = fact_table(N, MOD)
    f = fact[N - 1] * fact_inv[:N] % MOD * fact_inv[:N][::-1] % MOD
    

ans = 0
for k in range(K + 1):
    ans += (M * combinations_count(N - 1, k) * (M - 1) ** (N - 1 - k)) % mod

print(ans % mod)

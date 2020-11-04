from collections import defaultdict


def solve(input_s: str):
    ans = 0
    n = len(input_s)
    mod = 2019
    dp = defaultdict(int)
    cur = 0
    for i in range(n, -1, -1):
        if i == n:
            dp[0] += 1
        else:
            # cur += ((10 ** (n - i - 1)) * int(input_s[i])) % mod これはnがでかくなるとめちゃめちゃ遅い
            cur += pow(10, n - i - 1, 2019) * int(input_s[i]) % mod
            cur %= mod
            dp[cur] += 1
    for v in dp.values():
        if v > 1:
            ans += v * (v - 1) // 2
    return ans


if __name__ == '__main__':
    S = input()
    '''
    with open(sys.argv[1], 'r') as f:
        S = f.readline().strip()
    '''
    print(solve(S))

from collections import defaultdict
from math import gcd


def main():
    mod = 10 ** 9 + 7
    worst_iwashi_count = 0
    ans = 1
    d = defaultdict(int)
    N = int(input())
    for _ in range(N):
        a, b = map(int, input().split())
        if a == 0 and b == 0:
            worst_iwashi_count += 1
        elif a == 0:
            d[(0, -1)] += 1
        elif b == 0:
            d[(1, 0)] += 1
        else:
            g = gcd(abs(a), abs(b))
            if a * b > 0:
                d[(abs(a // g), abs(b // g))] += 1
            else:
                d[(abs(a // g), -abs(b // g))] += 1
    done_set = set()
    for a, b in list(d):
        if (a, b) in done_set:
            continue
        x = d[(a, b)]
        done_set.add((a, b))
        if b >= 0:
            y = d[(b, -a)]
            done_set.add((b, -a))
        else:
            y = d[(-b, a)]
            done_set.add((-b, a))
        ans *= 2 ** x + 2 ** y - 1
        ans %= mod
    ans += worst_iwashi_count - 1
    print(ans % mod)


if __name__ == '__main__':
    main()

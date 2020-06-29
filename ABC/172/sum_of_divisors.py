N = int(input())


def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1

    return len(lower_divisors) + len(upper_divisors)


ans = 0
for i in range(N):
    ans += (i+1) * make_divisors(i+1)
print(ans)

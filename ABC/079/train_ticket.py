S = input()
n = len(S)
# bit全探索
for i in range(2 ** (n - 1)):
    ope = S
    cur = 0
    for j in range(n - 1):
        if (i >> j) & 1:
            ope = ope[:-j - cur - 1] + '+' + ope[-j - cur - 1:]
        else:
            ope = ope[:-j - cur - 1] + '-' + ope[-j - cur - 1:]
        cur += 1
    if eval(ope) == 7:
        print(ope + '=7')
        break
